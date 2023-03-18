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

    def test_inheritance(self):
        """Tests inheritance."""
        basemodel = BaseModel()
        self.assertIsInstance(BaseModel, BaseModel)

    def test_name_attribute(self):
        """Tests the name attribute."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')


if __name__ == '__main__':
    unittest.main()
