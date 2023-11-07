#!/usr/bin/python3
"""
This returns an object represented by JSON string
"""


import json


def from_json_string(my_str):
    """
    Returns object represented by my_str
    """

    return json.loads(my_str)
