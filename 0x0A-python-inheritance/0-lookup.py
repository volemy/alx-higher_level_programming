#!/usr/bin/python3
"""
Module 0-lookup:
This module provides a function to returns a list of attributes and methods associated with an object.
"""


def lookup(obj):
    """
    Obtain a list of attributes and methods of the given object.

    Parameters:
    obj (any): The object for which you wish to retrieve attributes and methods.

    Returns:
    list: A list of strings containing the names of attributes and methods
          linked to the provided object, `obj`.
    """
    return dir(obj)
