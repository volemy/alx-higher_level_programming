#!/usr/bin/python3
"""
This checks if an object is an instance of a class
"""

def is_kind_of_class(obj, a_class):
    """ This returns True if object is an instance of a class
    that inherited from otherwise False"""
    return isinstance(obj, a_class)
