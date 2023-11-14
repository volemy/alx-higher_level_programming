#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Unitest to test instantiation"""

    def test_constructor_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_constructor_with_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_incrementing_nb_objects(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_nd_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(13).__nb_objects)

    def test_float_id(self):
        b1 = Base(1.5)
        self.assertEqual(b1.id, 1.5)

    def test_str_id(self):
        b1 = Base("string")
        self.assertEqual(b1.id, "string")

    def test_bool_id(self):
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_list_id(self):
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_dict_id(self):
        b1 = Base({"key": "value"})
        self.assertEqual(b1.id, {"key": "value"})


class TestBase_to_json_string(unittest.TestCase):
    """Unittest to test to_json_string in base.py"""

    def test_to_json_string_list(self):
        list_dictionaries = [{"key": "value"}, {"key": "value2"}]
        json_dictionary = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_dictionary, '[{"key": "value"}, {"key": "value2"}]')

    def test_to_json_string_dict(self):
        dictionary = {"key": "value"}
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '{"key": "value"}')

    def test_to_json_string_empty_list(self):
        list_dictionaries = []
        json_dictionary = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_dictionary, '[]')

    def test_to_json_string_empty_dict(self):
        dictionary = {}
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '[]')

    def test_to_json_string_None(self):
        list_dictionaries = None
        json_dictionary = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_dictionary, '[]')

    class TestBase_save_to_file(unittest.TestCase):
    """Unittest to test save_to_file in base.py"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        with open("Base.json", "w") as f:
            f.write("[]")

    def test_save_to_file_empty_list(self):
        list_objs = []
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_dict(self):
        list_objs = {}
        Base.save_to_file(None)
        A
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_None(self):
        list_objs = None
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")


class TestBase_from_json_string(unittest.TestCase):
    """Unittest to test from_json_string in base.py"""

    def test_from_json_string_None(self):
        json_string = None
        list_dictionaries = Base.from_json_string(json_string)
        self.assertEqual(list_dictionaries, [])

    def test_from_json_string_empty(self):
        json_string = "[]"
        list_dictionaries = Base.from_json_string(json_string)
        self.assertEqual(list_dictionaries, [])

    def test_from_json_string_one(self):
        json_string = '[{"key": "value"}]'
        list_dictionaries = Base.from_json_string(json_string)
        self.assertEqual(list_dictionaries, [{"key": "value"}])

    def test_from_json_string_two(self):
        json_string = '[{"key": "value"}, {"key": "value2"}]'
        list_dictionaries = Base.from_json_string(json_string)
        self.assertEqual(list_dictionaries, [{"key": "value"}, {"key": "value2"}])

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittest to test create in base.py"""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 1/2 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 1/2 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittest to test load_from_file in base.py"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        with open("Base.json", "w") as f:
            f.write("[]")

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittest to test save_to_file_csv in base.py"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        with open("Base.json", "w") as f:
            f.write("[]")

    def test_save_to_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_save_to_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_save_to_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_save_to_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_save_to_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_save_to_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittest to test load_from_file_csv in base.py"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        with open("Base.json", "w") as f:
            f.write("[]")

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

if __name__ == '__main__':
    unittest.main()

