#!/usr/bin/python3
"""
This returns the dictionary with simple data structure
"""


def class_to_json(obj):
    """
    This creates a dictionary desription of object
    """

    return obj.__dict__
