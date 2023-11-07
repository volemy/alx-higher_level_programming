#!/usr/bin/python3
"""
This function reads a text file(UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads from filename and prints contents to stdout
    """

    with open(filename, encoding="utf8") as f:
        read_text = f.read()
        print(read_text, end="")
