#!/usr/bin/python3
"""Test for User Class."""
import unittest
from models.user import User
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test instances and methods from User class."""

    a = User()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance(self):
        """Tests inheritance."""
        user = User()
        self.assertIsInstance(User, BaseModel)

    def test_name_attribute(self):
        """Tests the name attribute."""
        user = User()
        self.assertTrue(hasattr(User, 'name'))
        self.assertEqual(User.name, '')


if __name__ == '__main__':
    unittest.main()
