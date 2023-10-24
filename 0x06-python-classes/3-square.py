#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the Square
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int, optional): size of a side of the Square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
            """Returns the area of the square.

            Returns:
                int: the area of the square
            """

            return (self.__size * self.__size)
