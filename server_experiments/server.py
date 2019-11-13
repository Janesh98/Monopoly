import socket
import threading
import sys

'''
The server can send commands to clients in a format:
"<player_id> <command> <args>" or "<print/id> <string/digits>\n"
commands: print, id, move, name
'''

class Player():
    def __init__(self, conn, player_name=None, pos=None):
        self.conn = conn
        self.name = player_name
        self.player_id = get_addr(conn)[1]
        self.is_ready = False           #used for starting game when all players are ready
        self.is_turn = False            #is it this players turn?
        if pos == None:
            self.pos = [0, 0]
        else:
            self.pos = pos
    
    def name(self, name):                   #sets name of a player
        self.name = name
        message = "{} name {}\n".format(self.player_id, name)
        broadcast(message)
        print(message, endl="")
    
    def move(self, new_pos):                #move a player on a grid
        tmp = new_pos.split()
        for i in range(len(self.pos)):
            self.pos[i] = int(tmp[i])
        
        message = "{} move {}\n".format(self.player_id, new_pos)
        broadcast(message)
        print(message, endl="")
    
    def client_command(self, command):
        print(self.player_id, command)                          #prints command sent
        tokens = command.strip().split(" ", 1)                  #splits on first space
        try:
            if tokens[0] in self.commands_nullary.keys():       #checks if the first word is a command
                self.commands_nullary[tokens[0]](self)
            elif tokens[0] in self.commands_unary.keys():
                self.commands_unary[tokens[0]](self,tokens[1])
            else:
                #if command not recognised, send message
                message = "print Command not recognised: '{}'\n".format(tokens[0])
                send_message(self.conn, message)
                print(message, endl="")
        except IndexError:
            #if used wrong arguments, send message
            message = "print Wrong use of command: '{}'\n".format(tokens[0])
            send_message(self.conn, message)
            print(message, endl="")
    
    def echo_addr(self):        #sends clients address
        send_message(self.conn, "print Your address: {}\n".format(get_addr(self.conn)))
    
    def echo(self, message):    #echos back message
        send_message(self.conn, "print {}\n".format(message))
    
    def info(self):             #returns commands setting up a player class
        return "{0} name {1}\n{0} move {2} {3}\n".format(self.player_id, self.name, self.pos[0], self.pos[1])
        
    #dictionaried used in client_command
    commands_nullary = {
        "address": echo_addr
    }
        
    commands_unary = {
        "move": move,
        "name": name,
        "echo": echo
    }


#socket setup

ip_addr = ""
port = 8001

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_running = True

socket_details = (ip_addr,port)
serversocket.bind(socket_details)
serversocket.listen(6)

connected_devices = {}

def send_server_info(conn):             #used for setting up the client to the servers current state
    server_info = ""
    for c, dic in connected_devices.items():
        server_info += dic["player"].info()     #gets info about every player
    send_message(conn, server_info)
    print("Sent server info to {}".format(dic["addr"]))

def start_client_thread(conn,address):          #starts client thread that listens to a client
    th = threading.Thread(target=client_thread ,args=(conn,address))
    th.start()
    connected_devices[conn]["thread"] = th
    connected_devices[conn]["player"] = Player(conn)    #creates player object
    

#all send and broadcast messages must end with a "\n" in case 2 packets combine
def broadcast(message, original_conn=None):
    for conn in connected_devices:
        if conn != original_conn:
            conn.send(message.encode())

def send_message(conn, message):
    conn.send(message.encode())

def get_addr(conn):
    return connected_devices[conn]["addr"]
    

def client_thread(conn, addr):
    #broadcast to other clients that a new player joined
    broadcast(str(addr[1]) + "\n")
    
    #send server info (setup client)
    send_server_info(conn)
    #welcome message and client id
    send_message(conn, "print Welcome, input your name 'name <your name>'\nid {}\n".format(addr[1]))
    
    while server_running:
        try:
            message = conn.recv(1024)           #receive client commands
            if message:
                enc_message = message.decode()
                connected_devices[conn]["player"].client_command(enc_message)   #process client commands
            else:
                pass
        except:
            pass

#main loop
try:
    while True:
        conn , addr = serversocket.accept()         #accept new client
        connected_devices[conn] = {"addr" :addr}    #put into a dictionary
        print("{} connected".format(addr))
        start_client_thread(conn, addr)
except KeyboardInterrupt:           #shutdown server by ^C
    print(" Server shutting down")
    for conn in connected_devices:
        conn.close()                #closes all connections
    serversocket.close()
    server_running = False
    sys.exit(0)
