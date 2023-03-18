#!/usr/bin/python3
"""Test for Place Class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test instances and methods from Place class."""

    a = Place()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance(self):
        """Tests inheritance."""
        amenity = Place()
        self.assertIsInstance(Place, BaseModel)

    def test_name_attribute(self):
        """Tests the name attribute."""
        amenity = Place()
        self.assertTrue(hasattr(Place, 'name'))
        self.assertEqual(Place.name, '')


if __name__ == '__main__':
    unittest.main()
