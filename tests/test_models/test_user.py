#!/usr/bin/python3
"""Test for User Class."""
import unittest
from models.user import User
import datetime
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Test instances and methods from User class."""

    a = User()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.a)), res)
