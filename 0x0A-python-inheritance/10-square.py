#!/usr/bin/python3
"""
A sub-class square that is inherited from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A sub-class that inherits from Rectangle
    """

    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """This returns string of aquare instance"""
        return super().__str__()

    def area(self):
        """
        This returns the area of Square instance
        and overwrites the area() method from BaseGeometry
        """
        return self.__size ** 2
