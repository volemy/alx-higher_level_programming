#!/usr/bin/python3
"""
This appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    This appends a string to the end of a text file in UTF-8 encoding
    and retruns the number of characters addded.
    """

    with open(filename, mode='a', encoding='utf-8') as file:
        num_characters_added = file.write(text)

    return num_characters_added
