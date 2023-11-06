#!/usr/bin/python3
"""
This is a inherits_from module
"""


def inherits_from(obj, a_class):
    """
    This checks if the object is an instance of a class (directly or
    indirectly)
    """
    return isinstance(obj, a_class) and type(obj) != a_class
