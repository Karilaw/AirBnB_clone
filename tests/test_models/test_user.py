#!/usr/bin/env python3
"""
Unit tests for the User class.
"""

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up the environment before each test case."""
        self.user = User()

    def tearDown(self):
        """Clean up the environment after each test case if needed."""
        self.user = None

    def test_user_attributes(self):
        """Test if the User instance has the required attributes."""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_inheritance(self):
        """Test if the User instance is an instance of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_user(self):
        """Test the User class."""
        user = User(
            email='user@example.com',
            password='password123',
            first_name='John',
            last_name='Doe'
        )
        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

if __name__ == '__main__':
    unittest.main()

