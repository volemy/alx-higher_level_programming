#!/usr/bin/python3
"""1-square.py"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the Square
    """

    def __init__(self, size: int) -> None:
        """Initialize a new Square.

        Args:
            size (int): size of a side of the Square

        Return:
            None
        """
        self.__size = size
