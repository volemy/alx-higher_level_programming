#!/usr/bin/python3
from sys import argv

def print_args(argv):

    num_args = len(argv) - 1
    if num_args == 0:
        print(f"{num_args:d} arguments.")
    elif num_args == 1:
        print(f"{num_args:d} argument:")
    else:
        print(f"{num_args:d} arguments:")

    for i in range(1, num_args + 1):
        print(f"{i:d}: {argv[i]:s}")

if __name__ == "__main__":
    print_args(argv)
