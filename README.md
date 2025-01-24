# Service-Exchange-Keys-101
An introductory assignment for learning public/private-key exchange.

Difficulty: Medium.

Recommended level:
- Ability to code and understand python
- Some basic understanding of networks

Please read [Background.md](https://github.com/mzen17/SEP01-HW/blob/main/Background.md) to gain some understanding of Key-Exchange.

## Environment Setup
Linux + Python3 + Git. Other environments not tested, but all UNIX environments should work.

Run the following:

```
git clone https://github.com/mzen17/SEP01-HW.git
cd SEP01-HW
sudo python3 -m test.py
```

Why does this program need sudo? [It turns out, to create a socket in Linux, one needs root access](https://security.stackexchange.com/questions/244635/why-do-i-need-root-privileges-to-send-a-raw-packet-from-a-unix-machine).

## Notes
- You should only be modifying the client.py file. Other files are system libraries.
- Sometimes the code will hang. Ctrl+C to quit.

This is what tests passing should look like:

![image](https://github.com/user-attachments/assets/4306973e-4f3f-40d4-b3ea-7cf59f3ac707)


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
