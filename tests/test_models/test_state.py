#!/usr/bin/python3
"""Test for State Class."""
import unittest
from models.state import State
from models.user import User
from models.amenity import Amenity


class TestState(unittest.TestCase):
    """Tests instances and methods from State class."""

    def test_name_attribute_has_correct_default_value(self):
        """Function tests that the name attribute."""
        amenity = Amenity()
        self.assertEqual("", amenity.name)

    def test_name_assignment(self):
        """Test that the name of a function is correctly assigned."""
        amenity = Amenity()
        amenity.name = "new name"
        self.assertEqual("new name", amenity.name)


if __name__ == '__main__':
    unittest.main()
