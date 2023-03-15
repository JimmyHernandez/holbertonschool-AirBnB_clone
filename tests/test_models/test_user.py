#!/usr/bin/python3
"""Test for User Class."""
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """Tests instances and methods from User class"""

    a = User()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.a)), res)
