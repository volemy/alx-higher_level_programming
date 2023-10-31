#!/usr/bin/python3
"""
This is the add integer module add_integer(a, b=98)
The function add_integer for this module returns the sum of a and b
a and b must be integers or floats
If the input is not valid, TypeError is raised
"""

def add_integer(a, b=98):
    """
    This adds two integers and returns the sum as the result.

    Attributes:
        a (int or float): first numeric value
        b (int or float): second numeric value, defaults to 98
    Returns:
        the sum of a and b

    Raises:
        TypeError: if either a or b is not an integer or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a  must be an integer")
    if not isinstance(b, (int,float)):
        raise TypeError("b  must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
