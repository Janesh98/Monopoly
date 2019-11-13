import socket
import select
import sys

'''
name <your playr name>          #sets name of player
move <int> <int>                #change position on a 2D grid
list                            #display all local player objects
echo <message>                  #echo back a message
address                         #get your IP address
'''

#setup server connection
ip_address = "127.0.0.1"
port = 8001

server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.connect((ip_address,port))

class Player():
    def __init__(self, player_id, player_name=None, pos=None):
        self.name = player_name
        self.player_id = player_id
        self.is_ready = False           #used for starting game when all players are ready
        self.is_turn = False            #is it this players turn?
        if pos == None:
            self.pos = [0, 0]
        else:
            self.pos = pos
    
    def name(self, name):                   #sets name of a player
        self.name = name
    
    def move(self, new_pos):                #move a player on a grid
        tmp = new_pos.split()
        for i in range(len(self.pos)):
            self.pos[i] = int(tmp[i])
    
    def client_command(self, command):      #process commands from server
        tokens = command.strip().split(" ", 1)
        try:
            if tokens[0] in self.commands_nullary.keys():
                self.commands_nullary[tokens[0]](self)
            elif tokens[0] in self.commands_unary.keys():
                self.commands_unary[tokens[0]](self,tokens[1])
            else:
                print("Command from server not recognised: '{}'".format(tokens[0]))     #should never happen
        except IndexError:
            print("Server input error at: '{}'".format(tokens[0]))                      #should never happen
    
    def __str__(self):          #returns a formated information about player
        return ("name: {}\n"
                "id: {}\n"
                "pos: {}").format(self.name, self.player_id, self.pos)
    
    commands_nullary = {}
        
    commands_unary = {
        "move": move,
        "name": name,
    }

local_player_id = None      #current clients player id
players = {}                #dictionary of players by player_id


def server_input(commands):
    for command in commands.strip().split("\n"):
        tokens = command.strip().split(" ", 1)
        if tokens[0].isdigit():                                          #if player id given as first arg
            int_id = int(tokens[0])
            if len(tokens) > 1:
                if int_id in players.keys():                             #if player exists
                    players[int_id].client_command(tokens[1])            #do command in a player object
                else:
                    players[int_id] = Player(int_id)                           #else make a new player and do command
                    players[int_id].client_command(tokens[1])
            else:
                players[int_id] = Player(int_id)                               #if only id given, make new player
        elif tokens[0] == "print":          #print to client
            print(tokens[1])
        elif tokens[0] == "id":             #set local_player_id to conn adderss id
            local_player_id = int(tokens[1])
        else:
            print("unrecognised server command: '{}'".format(command))

inputs = [sys.stdin, server_connection]

#main loop
while True:
    try:
        read, write, error = select.select(inputs, [], [])
        for data_input in read:
            if data_input == server_connection:         #if server sent message
                message = data_input.recv(1024)
                parsed_message = message.decode()
                if parsed_message != '':
                    server_input(parsed_message)        #processes command from server
                #    print(parsed_message)
            else:
                message = sys.stdin.readline()
                if message.strip() == "list":           #if command = "list", display players
                    #display all players
                    print("#"*20)
                    for p in sorted(players.values(), key=lambda x:x.player_id):
                        print(p)
                        print("-"*20)
                else:                                   #otherwise send command to server
                    server_connection.send(message.strip().encode())
                    sys.stdout.flush()
            
    except KeyboardInterrupt:
        server_connection.close()
        print("disconnected")
        sys.exit(0)
