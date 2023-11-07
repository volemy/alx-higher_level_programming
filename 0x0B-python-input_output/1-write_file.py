#!/usr/bin/python3
"""
this function writes a string to a text file and returns number of
characters
"""


def write_file(filename="", text=""):
    """
    writes a string to text file in UTF-8 and returns number of
    characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
