import socket
import select
import sys

class Client():
    def __init__(self, address, port):
        self.address = address
        self.port = int(port)
        self.connected = False
        self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def establish_connection(self, address, port):
        try:
            self.server_connection.connect((address, port))
            self.connected = True
        except ConnectionRefusedError:
            print("Couldin't connect to server")
    
    def send_server(self, message):
        self.server_connection.send(message.strip().encode())
    
    def run(self):
    
        self.establish_connection(self.address, self.port)
        
        ##########  SETUP TKINTER HERE  #############
        
        #sys.stdin temporary, use tkinter instead
        inputs = [sys.stdin, self.server_connection]
        
        while self.connected:       #Main game loop
        
            ######  DISPLAY TKINTER HERE  ########
            
            
            #asking for input, server or tkinter
            try:
                read, write, error = select.select(inputs, [], [])
                for data_input in read:
                    if data_input == self.server_connection:         #if server sent message
                        message = data_input.recv(2048)
                        parsed_message = message.decode()
                        if parsed_message != '':
                            print(parsed_message)   #print message from server, temporary
                            #
                            #display.process_command(parsed_message)        #processes command from server
                            #
                    else:
                        #
                        #Input from tkinter gets sent to server
                        #
                        self.send_server(sys.stdin.readline())
                        sys.stdout.flush()
                    
            except KeyboardInterrupt:
                self.server_connection.close()
                self.connected = False
                print("disconnected")

if __name__ == "__main__":
    c = Client(sys.argv[1], sys.argv[2])
    c.run()
