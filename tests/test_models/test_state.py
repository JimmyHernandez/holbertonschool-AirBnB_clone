#!/usr/bin/python3
"""Test for State Class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests instances and methods from State class."""

    a = State()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.a)), res)
