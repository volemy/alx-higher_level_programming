#!/usr/bin/python3
"""
unittest for max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    this is the testcase for the max_integer function
    """

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 3, 5, -7]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 3.7, 5.2]), 5.2)

    def test_mixed_types(self):
        self.assertEqual(max_integer([1, 3, "5", 7]), 7)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_empty_string(self):
        self.assertEqual(max_integer([""]), "")

if __name__ == '__main__':
    unittest.main()
