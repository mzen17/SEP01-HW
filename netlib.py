"""
Network library for this project.
Do not modify if you are doing the assignment--it will break it.
"""

import socket


def init_connection(host: str, port: int):
    """
    Initialize a socket connection to host.
    host -- str containing hostname
    port -- port
    Returns socket obect
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket


def send_recv(host: str, port: int, message: str):
    """Send a message and recieve a response.
    message - the str to send
    type - REQ SAT (request SAT) or FUNC (enable encryption)
    Returns response.
    """
    cs = init_connection(host, port)
    cs.send(message.encode())
    response = cs.recv(1024).decode()
    cs.close()
    return response
