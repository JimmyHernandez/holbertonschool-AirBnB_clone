#!/usr/bin/python3
"""Test for City Class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests instances and methods from City class"""

    a = City()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.a)), res)
