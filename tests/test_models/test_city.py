#!/usr/bin/env python3
"""Test cases for the City class."""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up the environment before each test case."""
        self.city = City()

    def tearDown(self):
        """Clean up the environment after each test case if needed."""
        self.city = None

    def test_city_attributes(self):
        """Test if the City instance has the required attributes."""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_inheritance(self):
        """Test if the City instance is an instance of BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_city(self):
        """Test the City class."""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.state_id, 'CA')
        self.assertEqual(city.name, 'San Francisco')


if __name__ == '__main__':
    unittest.main()
