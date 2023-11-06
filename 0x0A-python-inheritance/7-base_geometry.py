#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """ This class has public instance methods """
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This validates values and assumes name is a string
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
