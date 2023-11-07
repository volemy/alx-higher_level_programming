#!/usr/bin/python3
"""
This cretaes an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    This creates an object from filename
    """

    with open(filename, mode='r') as file:
        loaded_obj = json.load(file)
    return loaded_obj
