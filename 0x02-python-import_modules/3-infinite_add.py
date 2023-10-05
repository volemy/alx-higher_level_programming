#!/usr/bin/python3
from sys import argv

def sum_args(argv):

    sum = 0
    for arg in argv[1:]:
        sum += int(arg)
    return sum

if __name__ == "__main__":
    print(sum_args(argv))
