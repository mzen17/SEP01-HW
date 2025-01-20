"""
Test.py is a program for testing your application.
Do not modify this program.
"""

import threading
from client import solve_SAT_problem1, solve_SAT_problem2
from program import ServerThread, MANThread
import socket
import time
import random

online = True
sniff_flags = []

# these generate 2 random ports.
# Your testing may fail due to ports being used. 
# If so, re-run tests.
# Why is this used? This is used to avoid TCP wait states during quick restarts.
# https://superuser.com/questions/173535/what-are-close-wait-and-time-wait-states
port1 = random.randint(1, 10000) + 1000
port2 = random.randint(1, 10000) + 1000

print(f"Using ports {port1} | {port2}")

# create the server + man using generated ports from above
main_server = ServerThread("127.0.0.1", port1)
main_server.start()

m_middle = MANThread("127.0.0.1", port2, port1, 1)
m_middle.start()

def test1():
    ans = solve_SAT_problem1(port=port1)
    # peer2peer comms since no sniffs
    if (ans == 1900):
        print("Test 1: Passed.")
    else:
        print("Test 1: Failed.")
        print("Your answer: " + str(ans))
        print("Correct Answer: 1900")

def test2():
    ans = solve_SAT_problem2(port=port2)
    # man detect SATS
    if (ans == 1900) and m_middle.get_flags() == []:
        print("Test 2: Passed.")
    elif ( ans == 1900):
        print("Test 2: Failed.")
        print("The SAT was sniffed.")
    else:
        print("Test 2: Failed.")
        print("Your answer: " + str(ans))
        print("Correct Answer: 1900")

time.sleep(1)
test2()

# stop servers after tests to clean
m_middle.kill()
main_server.kill()
print("Shutting down...")