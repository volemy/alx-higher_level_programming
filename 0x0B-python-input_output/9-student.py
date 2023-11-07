#!/usr/bin/python3
"""
This module creates a student class
"""


class Student:
    """
    This class defines a student
    public attributes:
        - first_name
        _ last_name
        _ age

    """

    def __init__(self, first_name, last_name, age):
        """
        instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This returns a dictionary representation of an instance
        """
        return self.__dict__
