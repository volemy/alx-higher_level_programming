#!/usr/bin/python3
"""
This module defines a function for introducing a person with their name.
"""

def say_my_name(first_name, last_name=""):
    """
    This function prints a message introducing a person.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person (default is an empty string).

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        raise TypeError(
        "{:s} must be a string".format(
            "first_name" if isinstance(last_name, str) else "last_name"
            )
        )
