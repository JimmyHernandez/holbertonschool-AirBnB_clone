#!/usr/bin/python3
"""Tests for BaseModel, City, and Place Classes."""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test instances and methods from Place class."""

    def setUp(self):
        """Set up the test case."""
        self.a = Place()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.a)), res)


if __name__ == '__main__':
    unittest.main()
