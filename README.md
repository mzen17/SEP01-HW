# Service-Exchange-Keys-101
An introductory assignment for learning public/private-key exchange.

Difficulty: Medium.

Recommended level:
- Ability to code and understand python
- Some basic understanding of networks

Please read [Background.md](https://github.com/mzen17/SEP01-HW/blob/main/Background.md) to gain some understanding of Key-Exchange.

## Environment Setup
Linux + Python3. Other environments not tested, but all UNIX environments should work.

Run `sudo python3 -m test.py`.

Why does this program need sudo? [It turns out, to create a socket in Linux, one needs root access](https://security.stackexchange.com/questions/244635/why-do-i-need-root-privileges-to-send-a-raw-packet-from-a-unix-machine).

## Notes
- You should only be modifying the client.py file. Other files are system libraries.
- Some files are 

## Task 1
- Implement SAT sharing with basic calculations.
- Ensure it says test1 passed.

## Task 2
- Implement decrypt and encrypt for strings->int and int->string
- Utilize it during SAT sharing.
- Ensure test2 passes.

## Task 3
IP.

# Discussion and need help?
We will review the program in lecture.

Post questions on the discord!