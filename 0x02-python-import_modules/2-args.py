#!/usr/bin/python3
import sys

if __name__ == "__main__":
    infinite = sys.argv[1:]
    sum = 0
    for i in infinite:
        sum += int(i)
    print(sum)
