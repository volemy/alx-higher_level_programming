#!/usr/bin/python3
"""
This module creates a student class.
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

    def to_json(self, attrs=None):
        """
        This returns a dictionary representation of an instance
        """

        my_dict = dict()
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            for attr in attrs:
                if attr in self.__dict__:
                    my_dict.update({attr: self.__dict__[attr]})
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        This replaces all attributes of student instance
        """

        for attr in json:
            self.__dict__.update({attr: json[attr]})
