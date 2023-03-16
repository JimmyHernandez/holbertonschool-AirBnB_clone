#!/usr/bin/python3
"""Test for Place Class."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test instances and methods from Place class."""

    a = Place()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.a)), res)
