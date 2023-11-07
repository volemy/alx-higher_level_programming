#!/usr/bin/python3
"""
This inserts line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This appends the new string after search_string in filename
    """

    with open(filename, mode="r") as file:
        text = file.readlines()

    with open(filename, mode="w") as file_to_write:
        s =""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        file_to_write.write(s)
