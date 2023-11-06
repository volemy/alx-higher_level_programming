#!/usr/bin/python3
"""
A sub-class Rectangle that is inherited from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A sub-class that inherits from the BaseGeometry
    """

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
