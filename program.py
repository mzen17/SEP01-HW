"""
This is the program running client.
It represents "Maria"
"""

import socket
import json
from client import basic_encrypt_decrypt
from netlib import send_recv
import time
import threading


maria_sat = 1000

class MANThread(threading.Thread):
    def __init__(self, ip_addr="127.0.0.1", i_port=5556, o_port=5555, tier=0):
        """Start MAN is a function to start a man-in-the-middle server.
        Note: IP for both MAN and external server must be the same.
        ip_addr -- IP address of server
        i_port -- port that MAN listens to (E.g, fake router port)
        o_port -- port that MAN forwards to (E.g, google) and returns
        flags -- Crucial information MAN sniffs
        onoff -- A flag to end MAN. It should be a list of [True] or [False]
        tier -- Tier of how strong it sniffs. 0 for off, 1 for regex scanning.
        """
        threading.Thread.__init__(self)
        self.ip_addr = ip_addr
        self.i_port = i_port
        self.o_port = o_port
        self.online = True
        self.flags = []
        self.tier = tier
    
    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(( self.ip_addr, self.i_port))
        server_socket.listen(10)
        server_socket.settimeout(3)

        while self.online:
            try:
                # Wait for a requester.
                client_socket, client_address = server_socket.accept()
                data = client_socket.recv(1024)

                val = data.decode('utf-8')
                response = send_recv(self.ip_addr, self.o_port, val)

                if "1500" in response or "1000" in response or "900" in response:
                    self.flags.append(True)

                # relay the data to the forward_port
                client_socket.send(response.encode('utf-8'))

            except Exception:
                pass

    def get_flags(self):
        return self.flags

    def kill(self):
        self.online = False

class ServerThread(threading.Thread):
    def __init__(self, ip_addr="127.0.0.1", port=5555):
        threading.Thread.__init__(self)
        self.ip_addr = ip_addr
        self.port = port
        self.online = True
        self.func = -1
    
    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(( self.ip_addr, self.port))
        server_socket.listen(10)
        server_socket.settimeout(3)

        while self.online:
            try:
                client_socket, client_address = server_socket.accept()
                data = client_socket.recv(1024)
                try:  
                    val = data.decode('utf-8')
                    if val == "SAT":
                        if self.func != -1:
                            response = basic_encrypt_decrypt(str(maria_sat), 1)
                        else:
                            response = str(maria_sat)
                    elif val == "FUNC":
                        self.func = 1
                        response = "SUCCESS"
            
                except Exception as e:
                    response = str(e)

                client_socket.send(response.encode('utf-8'))

            # Expected termination
            except Exception as e:
                pass
    
    def kill(self):
        self.online = False

