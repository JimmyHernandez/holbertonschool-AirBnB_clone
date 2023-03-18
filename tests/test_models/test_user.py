#!/usr/bin/python3
"""Test for User Class."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test instances and methods from User class."""

    def test_user_init(self):
        """Test if user instance initializes correctly."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")

    def test_user_attributes(self):
        """Test if user instance contains correct attributes."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_methods(self):
        """Test if user instance methods are working as expected."""
        user = User()
        user.email = "test@test.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict["email"], "test@test.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")
        self.assertEqual(user_dict["__class__"], "User")


if __name__ == '__main__':
    unittest.main()
