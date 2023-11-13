#!/usr/bin/python3
"""
This module contains the rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    This Rectangle class inherits from the Base module
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of the Rectangle class
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute
        """
        if not isinstance(value, int):
            raise TypError("y must be an integer")
        elif value < 0:
            raise ValueError("y  must be >= 0")
        self.__y = value

    def area(self):
        """
        This method calculates area of rectangle
        """
        return self.width * self.height
    def display(self):
        """
        Method to display the rectangle with '#'
        """
        for _ in range(self.height):
            print("#" * self.width)
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """
        This prints the Rectangle instance with '#' character in stdout
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        This assigns key/value argument to each attribute
        """
        if args and len(args) != 0:
            arg_index = 0
            for arg in args:
                if arg_index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_index == 1:
                    self.width = arg
                elif arg_index == 2:
                    self.height = arg
                elif arg_index == 3:
                    self.x = arg
                elif arg_index == 4:
                    self.y = arg
                arg_index += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

