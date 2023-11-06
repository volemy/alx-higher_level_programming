#!/usr/bin/python3
"""
This defines a class MyList.
"""


class MyList(list):
    """
    Custom list class that inherits from the built-in `list` class
    """

    def __init__(self):
        """
        This initializes a MyList object
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order
        """
        print(sorted(self))
