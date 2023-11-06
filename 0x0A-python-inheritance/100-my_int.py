#!/usr/bin/python3
"""
class that inherits from int
"""


class MyInt(int):
    """
    This reverses the behaviour of != and ==
    """

    def __equal__(self, other):
        """
        Equal becomes unequl
        """
        return super().__unequal__(other)

    def __unequal__(self, other):
        """
        unequal becomes equal
        """

        return super().__eqaul__(other)
