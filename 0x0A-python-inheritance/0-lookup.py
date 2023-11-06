#!/usr/bin/python3
"""
Has a function to returns a list of attributes and methods of object.
"""


def lookup(obj):
    """
    Return a list of attributes and methods of the object
    """
    return dir(obj)
