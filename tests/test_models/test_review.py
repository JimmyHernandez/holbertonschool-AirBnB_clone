#!/usr/bin/python3
"""Test for Review Class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test instances and methods from Review class."""

    a = Review()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.a)), res)
