#!/usr/bin/python3
"""Test class."""
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test_instantiation."""

    def test_attributes(self):
        """Test the attributes of the class."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Tests the str() function."""
        model = BaseModel()
        expected_output = "[{}] ({}) {}".format(
            model.__class__.__name__, model.id, model.__dict__)
        self.assertEqual(str(model), expected_output)

    def test_save(self):
        """Saves the current state of the model."""
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, prev_updated_at)

    def test_to_dict(self):
        """Converts a `Test` object to a dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.fromisoformat(
            model_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(
            model_dict['updated_at']), datetime)


if __name__ == '__main__':
    unittest.main()
