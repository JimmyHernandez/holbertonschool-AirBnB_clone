#!/usr/bin/python3
"""Test for City Class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test instances and methods from City class."""

    a = City()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance(self):
        """Tests inheritance."""
        state = City()
        self.assertIsInstance(City, BaseModel)

    def test_name_attribute(self):
        """Tests the name attribute."""
        state = City()
        self.assertTrue(hasattr(City, 'name'))
        self.assertEqual(City.name, '')


if __name__ == '__main__':
    unittest.main()
