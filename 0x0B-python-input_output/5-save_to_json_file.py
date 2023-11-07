#!/usr/bin/python3
"""
This writes an object to text file using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes a representation of my_obj
    """

    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
