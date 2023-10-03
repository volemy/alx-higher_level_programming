#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    if alphabet % 2 == 1:
        alphabet = alphabet - 32
    print("{:c}".format(alphabet), end="")
