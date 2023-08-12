#!/usr/bin/python3
"""
Unit tests for the State class.
"""


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up the environment before each test case."""
        self.state = State()

    def tearDown(self):
        """Clean up the environment after each test case if needed."""
        self.state = None

    def test_state_attributes(self):
        """Test if the State instance has the required attributes."""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_inheritance(self):
        """Test if the State instance is an instance of BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_state(self):
        """Test the State class."""
        state = State(name='California')
        self.assertEqual(state.name, 'California')


if __name__ == '__main__':
    unittest.main()
