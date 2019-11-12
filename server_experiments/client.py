import socket
import select
import sys

class Player():
    def __init__(self, player_id, player_name=None, pos=None):
        self.player_id = player_id
        self.name = player_name
        self.pos = pos

ip_address = "127.0.0.1"
port = 8001

server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.connect((ip_address,port))
print("client connected")

inputs = [sys.stdin, server_connection]

while True:
    try:
        read, write, error = select.select(inputs, [], [])
        for data_input in read:
            if data_input == server_connection:
                message = data_input.recv(1024)
                parsed_message = message.decode()
                if parsed_message != '':
                    print(parsed_message)
            else:
                message = sys.stdin.readline()
                server_connection.send(message.strip().encode())
                sys.stdout.flush()
            
    except KeyboardInterrupt:
        server_connection.close()
        print("disconnected")
        sys.exit(0)
