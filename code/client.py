import socket
import sys
import threading
import GUI as ui
import time

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = int(port)
        self.connected = False
        self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_thread = None
        self.ui_controls = None
        self.ui_root = None
        self.ui_ready = False
    
    
    def establish_connection(self, address, port):
        self.server_connection.connect((address, port))
        self.connected = True
        self.server_thread = threading.Thread(target=self.listen_thread)
        self.server_thread.start()
    
    
    def listen_thread(self):
        #wait for ui
        while not self.ui_ready:
            time.sleep(0.1)

        while self.connected:
            message = self.server_connection.recv(1024) #receive server commands
            if message:
                for command in message.decode().strip().split("\n"):
                    print(command)              #for debugging
                    #######  PROCESS COMMAND FROM SERVER  ########
                    if command == "kick":
                        self.connected = False
                    else:
                        self.ui_controls.process(command)
            else:
                pass
        
        self.server_connection.close()
        print("disconnected from server")
    
    def send_server(self, message):
        self.server_connection.send("{}\n".format(message.strip()).encode())
    
    def run(self):
        try:
            self.establish_connection(self.address, self.port)
            
            ##########  SETUP TKINTER HERE  #############
            ui.main(self)
            
            self.connected = False
            self.server_thread.join()

        except ConnectionRefusedError:
            print("Couldin't connect to server")


if __name__ == "__main__":
    c = Client(sys.argv[1], sys.argv[2])
    c.run()
