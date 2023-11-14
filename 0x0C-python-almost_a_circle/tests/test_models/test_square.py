#!/usr/bin/python3
"""Unittest for square.py
Unittest classes:
    TestSquareInstantiation
    TestSquareSize
    TestSquareX
    TestSquareY
    TestSquareArea
    TestSquareStdout
    TestSquareUpdateArgs
    TestSquareUpdateKwargs
    TestSquareDict
"""
import unittest
import sys
import io
from models.square import Square
from models.base import Base


class TestSquareInstantiation(unittest.TestCase):
    """Unittest for Square instantiation"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(1)
        s2 = Square(2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(2, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(1, 2, 3)
        s2 = Square(2, 2, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(2, 2, 3, 4)
        self.assertEqual(s1.id, s2.id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5)

    def test_size_setter(self):
        s1 = Square(1, 2, 3, 4)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_size_getter(self):
        s1 = Square(1, 2, 3, 4)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_width_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.width, 1)

    def test_height_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.height, 1)

    def test_x_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.x, 2)

    def test_y_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.y, 3)


class TestSquareSize(unittest.TestCase):
    """Unittest for Square size"""

    def test_None_size(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_str_size(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_float_size(self):
        with self.assertRaises(TypeError):
            Square(1.1)

    def test_list_size(self):
        with self.assertRaises(TypeError):
            Square([1])

    def test_tuple_size(self):
        with self.assertRaises(TypeError):
            Square((1,))

    def test_set_size(self):
        with self.assertRaises(TypeError):
            Square({1})

    def test_dict_size(self):
        with self.assertRaises(TypeError):
            Square({"a": 1})

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0, 2)


class TestSquareX(unittest.TestCase):
    """Unittest for Square x"""

    def test_None_x(self):
        with self.assertRaises(TypeError):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Square(1, "1")

    def test_float_x(self):
        with self.assertRaises(TypeError):
            Square(1, 1.1)

    def test_list_x(self):
        with self.assertRaises(TypeError):
            Square(1, [1])

    def test_tuple_x(self):
        with self.assertRaises(TypeError):
            Square(1, (1,))

    def test_set_x(self):
        with self.assertRaises(TypeError):
            Square(1, {1})

    def test_dict_x(self):
        with self.assertRaises(TypeError):
            Square(1, {"a": 1})

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -1)


class TestSquareY(unittest.TestCase):
    """Unittest for Square y"""

    def test_None_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "1")

    def test_float_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 1.1)

    def test_list_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, [1])

    def test_tuple_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, (1,))

    def test_set_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, {1})

    def test_dict_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, {"a": 1})

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -1)


class TestSquareArea(unittest.TestCase):
    """Unittest for Square area"""

    def test_area_singledigits(self):
        s1 = Square(1)
        self.assertEqual(s1.area(), 1)

    def test_area_doubledigits(self):
        s1 = Square(10)
        self.assertEqual(s1.area(), 100)

    def test_area_multidigits(self):
        s1 = Square(1000)
        self.assertEqual(s1.area(), 1000000)

    def test_area_changed_values(self):
        s1 = Square(10, 20, 30, 40)
        s1.size = 5
        self.assertEqual(s1.area(), 25)

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquareStdout(unittest.TestCase):
    """Unittest for testing __str__ and display methods of Square"""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.
        Args:
            sq (Square): The Square to print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test for __str__
    def test_square_str(self):
        s = Square(4)
        capture = TestSquareStdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_changed_values(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Test for display
    def test_display_width_height(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquareStdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquareStdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_width_height_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquareStdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittest for testing update args"""

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s.update(89, -1)

    def test_update_args_invalid_x_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            s.update(89, 2, "invalid")

    def test_update_args_y_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittest for testing update kwargs"""

    def test_update_kwargs_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2, x=3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2, x=3, y=4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_kwargs_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s.update(id=89, size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s.update(id=89, size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s.update(id=89, size=-1)

    def test_update_kwargs_invalid_x_type(self):
        s = Square(10, 10, 10,

class TestSquare_dict(unittest.TestCase):
    """Unittest for testing to_dictionary method of the Square class"""

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

