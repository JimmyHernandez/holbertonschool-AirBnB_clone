#!/usr/bin/python3
"""Test for State Class."""
import unittest
from models.state import State
from models.user import User


class TestState(unittest.TestCase):
    """Tests instances and methods from State class."""

    def test_name_attribute_has_correct_default_value(self):
        amenity = Amenity()
        self.assertEqual("", amenity.name)

    def test_name_assignment(self):
        amenity = Amenity()
        amenity.name = "new name"
        self.assertEqual("new name", amenity.name)


if __name__ == '__main__':
    unittest.main()
