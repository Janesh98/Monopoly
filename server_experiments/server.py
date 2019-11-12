import socket
import threading
import sys


class Player():
    def __init__(self, conn, player_id=0, player_name=None, pos=None):
        self.conn = conn
        self.player_id = player_id
        self.name = player_name
        if pos == None:
            self.pos = [0, 0]
        else:
            self.pos = pos
    
    def name(self, name):                   #sets name of a player
        self.name = name
        message = "Name set to: " + name
        send_message(conn, message)
        print(message)
    
    def move(self, new_pos):                #move a player on a grid
        if type(new_pos) == str:            #moving from string "num num"
            tmp = new_pos.split()
            for i in range(len(self.pos)):
                self.pos[i] = int(tmp[i])
        else:                               #moving from a tuple (int, int)
            for i in range(len(self.pos)):
                self.pos[i] = new_pos[i]
        
        message = "{} moved to: {}".format(self.name, self.pos)
        broadcast(message)
        print(message)
    
    def client_command(self, command):
        tokens = command.strip().split(" ", 1)
        try:
            if tokens[0] in self.commands_nullary.keys():
                self.commands_nullary[tokens[0]](self)
            elif tokens[0] in self.commands_unary.keys():
                self.commands_unary[tokens[0]](self,tokens[1])
            else:
                message = "Command not recognised: '{}'".format(tokens[0])
                send_message(self.conn, message)
                print(message)
        except IndexError:
            message = "Wrong use of command: '{}'".format(tokens[0])
            send_message(self.conn, message)
            print(message)
    
    def echo_addr(self):
        send_message(self.conn, "Your address: {}".format(get_addr(self.conn)))
    
    commands_nullary = {
        "address": echo_addr
    }
        
    commands_unary = {
        "move": move,
        "name": name
    }


ip_addr = "127.0.0.1"
port = 8001

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_running = True

socket_details = (ip_addr,port)
serversocket.bind(socket_details)
serversocket.listen(6)

connected_devices = {}

def start_client_thread(conn,address):
    th = threading.Thread(target=client_thread ,args=(conn,address))
    th.start()
    connected_devices[conn]["thread"] = th
    connected_devices[conn]["player"] = Player(conn, )
    
    #for c in connected_devices
    

def broadcast(message, original_conn=None):
    for conn in connected_devices:
        if conn != original_conn:
            conn.send(message.encode())

def send_message(conn, message):
    conn.send(message.encode())

def get_addr(conn):
    return connected_devices[conn]["addr"]
    

def client_thread(conn, addr):
    welcome = "Welcome, to input your name type 'name <your name>'"
    conn.send(welcome.encode())

    while server_running:
        try:
            message = conn.recv(1024)
            if message:
                enc_message = message.decode()
                print(enc_message)
                connected_devices[conn]["player"].client_command(enc_message)
                '''
                message_to_send = "<{}> {}".format(addr, enc_message.rstrip("\n"))
                print(message_to_send)
                broadcast(message_to_send, conn)
                '''
            else:
                pass	
        except:
            continue	

try:
    while True:
        conn , addr = serversocket.accept()
        connected_devices[conn] = {"addr" :addr}
        print("{} connected".format(addr))
        start_client_thread(conn, addr)
except KeyboardInterrupt:
    print(" Server shutting down")
    for conn in connected_devices:
        conn.close()
    serversocket.close()
    server_running = False
    sys.exit(0)
