#!/usr/bin/python3
"""Test for City Class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test instances and methods from City class."""

    a = City()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.a)), res)


if __name__ == '__main__':
    unittest.main()
