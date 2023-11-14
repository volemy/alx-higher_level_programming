#!/usr/bin/python3
"""This defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square
        Args:
            size (int): The size of the new Square
            x (int): The x coordinate of the new Square
            y (int): The y coordinate of the new Square
            id (int): The identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """This gets the size of the sqaure"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square
        Args:
            *args (ints): Arguments to update the Square
            **kwargs (dict): Keyword arguments to update the Square
        """
        if args and len(args) != 0:
            arg_index = 0
            for arg in args:
                if arg_index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_index == 1:
                    self.size = arg
                elif arg_index == 2:
                    self.x = arg
                elif arg_index == 3:
                    self.y = arg
                arg_index += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
