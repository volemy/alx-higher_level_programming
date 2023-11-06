#!/usr/bin/python3
"""
This returns True if object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Check if an object belongs to a specific class and returns
    True if the object belongs to the specified class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
