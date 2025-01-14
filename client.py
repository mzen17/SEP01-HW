"""
client.py is an example of a client program. This is [John]
Use: 'client.py 'ipaddr'
"""
import socket
from netlib import init_connection, send_recv

john_sat = 900

def basic_encrypt_decrypt(message: str, decode_encode_mode: int):
    """
    This is a function for managing strings.
    message -- the value you are sending
    decode_encode_mode -- 0 for decode (string -> int) or 1 for encode (int -> string)
    returns encrypted/decrypted value
    """

    summoned_value = None

    if decode_encode_mode == 0:
        # decode mode [task2]

        # transform the string back to the int value
        pass
    else:
        # encode mode [task2]
        
        # transform the int value to an encrypted string
        pass

    return summoned_value
    

def solve_SAT_problem1(host = '127.0.0.1', port = 5556):
    """
    solve_SAT_problem is a function that sends out a message to the host+port.
    Do not change the function name as tests require the name.
    """
    
    # Initialize the socket.
    # You may not know what sockets do. Ignore it.
    client_socket = init_connection(host, port)

    # Task 1 is almost solved for you.
    # Follow the following Pseudocode

    # Send and recieve a message of type REQ with parameters (SAT).
    # Add that recieve message to SAT score
    # return that score.

    # Functions you need to utilize:
    # - john_sat
    # - send_recv
    # - Return for returning output
    # send_recv is used like this: send_recv(client_socket, ["SAT" or "FUNC"])

    output = None # Modify this line of code
    
    client_socket.close()  # Close the connection
    return output

def solve_SAT_problem2():
    # Task 2 requires you to use the function value.
    # You need to implement a transform string to bypass detection.
    # Majority of the work will be in encrypt_SAT function.
    # The only work need to be done here is to first make a call with FUNC + False (utilize encryption)
    # Then make the call like you did in Task 1.

    # call 1
    # output = 
    pass