"""
Test.py is a program for testing your application.
Do not modify this program.
"""

import threading
from client import solve_SAT_problem1
from program import PKServer
from netlib import init_connection, send_recv, raw_sendrecv
import socket

failure = True

def runserver():
    pk = PKServer()
    pk.run()

def manProxy():
    man = ManInTheMiddleProxy()
    man.run()


class ManInTheMiddleProxy:
    """
    A malicious user trying to sell people's SAT scores that has hacked and gained access to the routers.
    """
    def __init__(self, ip_addr='127.0.0.1', listen_port=5556, forward_port=5555):
        # port 1
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(( ip_addr, listen_port))

        self.ip = ip_addr
        self.listen_port = listen_port
        self.forward_port = forward_port
        
        self.server_socket.listen(5)
        self.server_socket.listen(5)
        
        # If this is true, it has sniffed somebody's SAT.
        self.has_found_something = False

    def run(self):
        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                data = client_socket.recv(1024)

                try:  
                    sk = init_connection(self.ip, self.forward_port)
                    val = data.decode('utf-8')
                    response = raw_sendrecv(sk, val)

                except Exception as e:
                    response = str(e)
                # relay the data to the forward_port
                client_socket.send(response.encode('utf-8'))    


            # Expected termination
            except KeyboardInterrupt:
                print("Shutting down server...")
                break

# Create a thread
rserver = threading.Thread(target=runserver)
print("Starting rserver server")
rserver.start()
m_middle = threading.Thread(target=manProxy)

print("Starting MIM server")
m_middle.start()

def test1():
    ans = solve_SAT_problem1(port=5556)
    if (ans == 1900):
        print("Test 1: Passed.")
    else:
        print("Test 1: Failed.")

def test2():
    pass

def test3():
    pass

test1()