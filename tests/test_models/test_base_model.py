#!/usr/bin/python3
"""Test for Base Model Class."""
import unittest
from models.base_model import BaseModel


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
        basemodel = BaseModel()
        self.assertTrue(hasattr(BaseModel, 'name'))
        self.assertEqual(BaseModel.name, '')


if __name__ == '__main__':
    unittest.main()
