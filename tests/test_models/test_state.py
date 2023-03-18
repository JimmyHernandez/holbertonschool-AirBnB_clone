#!/usr/bin/python3
"""Test for State Class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests instances and methods from State class."""

    a = State()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance(self):
        """Tests inheritance."""
        state = State()
        self.assertIsInstance(State, BaseModel)

    def test_name_attribute(self):
        """Tests the name attribute."""
        state = State()
        self.assertTrue(hasattr(State, 'name'))
        self.assertEqual(State.name, '')


if __name__ == '__main__':
    unittest.main()
