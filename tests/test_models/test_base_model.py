#!/usr/bin/python3
"""Test for Base Model Class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """Test instances and methods from BaseModel class."""

    a = BaseModel()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(self.a)), res)

    def test_attribute_types(self):
        """Test attributes' data types."""
        a = Amenity()
        self.assertEqual(type(a.name), str)

    def test_has_attributes(self):
        """Test if attributes exists."""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))


if __name__ == '__main__':
    unittest.main()
