#!/usr/bin/python3
"""
This checks if an attribute can be added to an object
"""

def add_attribute(obj, a_attr, attr_value):
    """
    This adds a new attribute to an object if possible

    parameters
    obj (object): object which attribute should be added
    a_attr (str): Name of new attribute
    attr-value (any): Value of new attribute

    Raises
    TypeError: If object can't have new attributes
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, a_attr):
        raise TypeError("can't add new attribute")

    setattr(obj, a_attr, attr_value)

