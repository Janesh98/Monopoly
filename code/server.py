import socket
import threading
import sys

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
        
    def send_client(self, conn, message):
        conn.send(message.strip().encode())
        
    def send_all(self, message):
        for conn in self.connected_devices.keys():
            self.send_client(conn, message)
        
    def start_client_thread(self, conn, address):          #starts client thread that listens to a client
        th = threading.Thread(target=self.client_thread, args=(conn, address))
        th.start()
        self.connected_devices[conn]["thread"] = th
        #self.connected_devices[conn]["player"] = Player(conn)    #creates player object
    
    def client_thread(self, conn, addr):        #each thread connects to each client
        #broadcast to other clients that a new player joined
        #broadcast(str(addr[1]) + "\n")
        
        #send server info (setup client)
        #send_server_info(conn)
        #welcome message and client id
        self.send_client(conn, "Welcome")
        
        while self.server_running:
            try:
                message = conn.recv(1024)           #receive client commands
                if message:
                    dec_message = message.decode()
                    self.send_all(dec_message)      #echos message
                    print(dec_message)              #for debugging
                    #
                    #game.process_command(dec_message)
                    #
                    #connected_devices[conn]["player"].client_command(dec_message)   #process client commands
                else:
                    pass
            except:
                pass

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
