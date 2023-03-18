#!/usr/bin/python3
"""Test for Review class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test instances and methods from Amenity class."""

    def setUp(self):
        """Set up the test case."""
        self.a = Amenity()

    def test_class_exists(self):
        """Tests that the class exists."""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_name_attribute(self):
        """Test the name attribute."""
        self.assertTrue(hasattr(self.a, "name"))
        self.assertEqual(self.a.name, "")

        self.a.name = "pool"
        self.assertEqual(self.a.name, "pool")


if __name__ == '__main__':
    unittest.main()
