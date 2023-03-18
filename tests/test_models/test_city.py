#!/usr/bin/python3
"""Test for City Class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test instances and methods from City class."""

    def setUp(self):
        """Set up the test case."""
        self.city = City()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.city)), res)

    def test_name_attribute(self):
        """Test if City has a name attribute."""
        self.assertTrue(hasattr(self.city, "name"))

    def test_state_id_attribute(self):
        """Test if City has a state_id attribute."""
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_to_dict_method(self):
        """Test if to_dict method produces dictionary."""
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))

    def test_str_method(self):
        """Test if __str__ method produces string representation."""
        city_str = str(self.city)
        self.assertTrue(isinstance(city_str, str))


if __name__ == '__main__':
    unittest.main()
