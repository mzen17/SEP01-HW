"""
This is the program running client.
It represents "Maria"
"""

import socket
import json
from client import basic_encrypt_decrypt

maria_sat = 1000

class PKServer:
    def __init__(self, ip_addr="127.0.0.1" , port=5555):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(( ip_addr, port))
        self.ip = ip_addr
        self.port = port
        self.server_socket.listen(5)
        self.server_socket.listen(5)
        self.func = -1

    def run(self):
        print(f"Running on {self.ip}:{self.port}")
        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                data = client_socket.recv(1024)

                try:  
                    val = data.decode('utf-8')
                    print("Maria recv: " + str(val))
                    response = str(maria_sat)
                
                except Exception as e:
                    response = str(e)

                client_socket.send(response.encode('utf-8'))    

            # Expected termination
            except KeyboardInterrupt:
                print("Shutting down server...")
                break
