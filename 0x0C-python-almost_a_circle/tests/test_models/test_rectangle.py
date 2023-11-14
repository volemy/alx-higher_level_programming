#!/usr/bin/python3
"""
Defines unittests for models/rectangle.py

Unittest classes:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_order_of_i
    TestRectangle_area - line
    TestRectangle_update_args
    TestRectangle_update_kwargs
    TestRectangle_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Rectangle class
    """

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_width(unittest.TestCase):
    """
    Unittests for testing initialization of Rectangle width attribute
    """

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_boolean_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 1)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 1)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"hello", 1)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b"world"), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b"memory"), 1)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)

    def test_positive_width(self):
        r = Rectangle(7, 1)
        self.assertEqual(7, r.width)

    def test_zero_width(self):
        r = Rectangle(0, 2)
        self.assertEqual(0, r.width)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)


class TestRectangle_height(unittest.TestCase):
    """
    Unittests for testing initialization of Rectangle height attribute
    """

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))

    def test_boolean_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2, 3))

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, frozenset({1, 2, 3}))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b"hello")

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, bytearray(b"world"))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b"memory"))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_positive_height(self):
        r = Rectangle(1, 7)
        self.assertEqual(7, r.height)

    def test_zero_height(self):
        r = Rectangle(2, 0)
        self.assertEqual(0, r.height)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -5)


class TestRectangle_x(unittest.TestCase):
    """
    Unittests for testing initialization of Rectangle x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, None, 2)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 5, 5.5, 1)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, complex(5), 2)

    def test_boolean_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 1)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {"a": 1, "b": 2}, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 5, [1, 2, 3], 1)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, (1, 2, 3), 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 1)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, frozenset({1, 2, 3}), 2)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 5, b"hello", 1)

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, bytearray(b"world"), 2)

    def test_memoryview_x(self):
        with self

class TestRectangle_y(unittest.TestCase):
    """Unittests for testing y attribute of Rectangle class"""

    def test_None_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(4, 5, 6, "string")

    def test_float_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(7, 8, 9, 1.5)

    def test_complex_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(10, 11, 12, complex(1, 2))

    def test_list_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(13, 14, 15, [1, 2, 3])

    def test_dict_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(16, 17, 18, {"a": 1, "b": 2})

    def test_bool_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(19, 20, 21, True)

    def test_NaN_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(22, 23, 24, float("nan"))

    def test_negative_y(self):
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r = Rectangle(25, 26, 27, -1)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing area attribute of Rectangle class"""

    def test_area_singledigit(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.area(), 8)

    def test_area_doubledigit(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.area(), 1200)

    def test_area_multidigit(self):
        r = Rectangle(100, 200, 300, 400, 500)
        self.assertEqual(r.area(), 200000)

    def test_area_changed_values(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.width = 5
        r.height = 10
        self.assertEqual(r.area(), 500)

 class TestRectangleStr(unittest.TestCase):
    """Unittests for testing __str__ method and display of Rectangle class"""

    @staticmethod
    def capture_stdout(rect, method):
        """This captures the output of a method and returns  a string"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__
    def test_rectangle_str(self):
        r = Rectangle(8, 4, 2, 1, 7)
        self.assertEqual("[Rectangle] (7) 2/1 - 8/4", str(r))

    def test_str_changed_values(self):
        r = Rectangle(12, 18, 5, 7, 23)
        r.width = 3
        r.height = 6
        self.assertEqual("[Rectangle] (23) 5/7 - 3/6", str(r))

    # Test display
    def test_display_width_height(self):
        r = Rectangle(3, 2, 0, 0, 0)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("###\n###\n", catch.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(2, 3, 1, 0, 1)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", catch.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(5, 4, 0, 1, 0)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, catch.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(4, 2, 3, 2, 0)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, catch.getvalue())

class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittests for testing update args of Rectangle class"""

    def test_update_args_zero(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update()
        self.assertEqual("[Rectangle] (7) 2/1 - 8/4", str(r))

    def test_update_args_one(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(1)
        self.assertEqual("[Rectangle] (1) 2/1 - 8/4", str(r))

    def test_update_args_two(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(1, 3)
        self.assertEqual("[Rectangle] (1) 2/1 - 3/4", str(r))

    def test_update_args_three(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(1, 3, 5)
        self.assertEqual("[Rectangle] (1) 2/1 - 3/5", str(r))

    def test_update_args_four(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(1, 3, 5, 6)
        self.assertEqual("[Rectangle] (1) 6/1 - 3/5", str(r))

    def test_update_args_five(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(1, 3, 5, 6, 7)
        self.assertEqual("[Rectangle] (1) 6/7 - 3/5", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(None)
        correct = "[Rectangle] ({}) 2/1 - 8/4".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(1, "3")

    def test_update_args_invalid_height_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(1, 3, "5")

    def test_update_args_invalid_x_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(1, 3, 5, "6")

    def test_update_args_invalid_y_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r.update(1, 3, 5, 6, "7")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittests for testing  kwargs of Rectangle class"""

    def test_update_kwargs_one(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 2/1 - 8/4", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(id=1, width=3)
        self.assertEqual("[Rectangle] (1) 2/1 - 3/4", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(id=1, width=3, height=5)
        self.assertEqual("[Rectangle] (1) 2/1 - 3/5", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(id=1, width=3, height=5, x=6)
        self.assertEqual("[Rectangle] (1) 6/1 - 3/5", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(8, 4, 2, 1, 7)
        r.update(id=1, width=3, height=5, x=6, y=7)
        self.assertEqual("[Rectangle] (1) 6/7 - 3/5", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(id=1, width="3")

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(id=1, height="5")

    def test_update_kwargs_invalid_x_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(id=1, x="6")

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r.update(id=1, y="7")

class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of Rectangle class"""

    def test_to_dictionary_output(self):
        r = Rectangle(8, 4, 2, 1, 7)
        correct = {'x': 2, 'y': 1, 'id': 7, 'height': 4, 'width': 8}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(8, 4, 2, 1, 7)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(8, 4, 2, 1, 7)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

