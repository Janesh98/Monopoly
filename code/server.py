import socket
import threading
import sys
from random import randint
from board import Pawn

class Server:
    def __init__(self, port="8000", players=6):
        self.ip_addr = ""
        self.port = int(port)
        self.max_players = players
        self.connected_devices = {}
        self.server_running = True
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.server_socket.bind((self.ip_addr, self.port))
        self.server_socket.listen(players)
        
    def get_id(self, conn):
        return self.connected_devices[conn]["addr"][1]

    def send_client(self, conn, message):
        conn.send("{}\n".format(message.strip()).encode())  #each command split by \n
        
    def send_all(self, message, original_conn = None):
        for conn in self.connected_devices.keys():
            if conn != original_conn:
                self.send_client(conn, message)
        
    def start_client_thread(self, conn, address):          #starts client thread that listens to a client
        self.connected_devices[conn]["pawn"] = Pawn(address[1], 0, "cyan")      #creates pawn object
        self.send_all(self.connected_devices[conn]["pawn"].info(), conn)        #broadcast info about new pawn
        #start thread
        th = threading.Thread(target=self.client_thread, args=(conn, address))
        th.start()
        self.connected_devices[conn]["thread"] = th
   
    def process_command(self, conn, mess):
        if mess == "roll":
            d1 = randint(1, 6)
            d2 = randint(1, 6)
            self.send_client(conn, "roll {} {}".format(d1, d2))
            self.connected_devices[conn]["pawn"].move(d1 + d2)
            self.send_all("pawn {} move {}".format(self.get_id(conn), d1 + d2))

    def send_info(self, conn):  #used for initialising a client
        for dic in self.connected_devices.values():
            self.send_client(conn, dic["pawn"].info())

    def client_thread(self, conn, addr):        #each thread connects to each client
        #welcome message and client id
        self.send_client(conn, "Welcome")
        #send server info to client
        self.send_info(conn)
        
        while self.server_running:
            #try:
            message = conn.recv(1024)           #receive client commands
            if message:
                for command in message.decode().strip().split("\n"):
                    #self.send_all(dec_message)      #echos message
                    print(command)              #for debugging
                    #
                    self.process_command(conn, command)
                    #
                    #connected_devices[conn]["player"].client_command(dec_message)   #process client commands
            else:
                pass
            #except:
            #    pass

    def run(self):
        try:
            while True:
                conn , addr = self.server_socket.accept()           #accept new client
                self.connected_devices[conn] = {"addr" :addr}       #put into a dictionary
                print("{} connected".format(addr))
                self.start_client_thread(conn, addr)
        except KeyboardInterrupt:           #shutdown server by ^C
            print(" Server shutting down")
            for conn in self.connected_devices:
                conn.close()                #closes all connections
            self.server_socket.close()
            self.server_running = False

if __name__ == "__main__":
    s = Server(port=sys.argv[1])
    s.run()
