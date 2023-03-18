#!/usr/bin/python3
"""Test for Review Class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test instances and methods from Review class."""

    a = Review()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance(self):
        """Tests inheritance."""
        review = Review()
        self.assertIsInstance(Review, BaseModel)

    def test_name_attribute(self):
        """Tests the name attribute."""
        review = Review()
        self.assertTrue(hasattr(Review, 'name'))
        self.assertEqual(Review.name, '')


if __name__ == '__main__':
    unittest.main()
