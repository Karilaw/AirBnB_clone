#!/usr/bin/python3
"""Unit tests for the Amenity class."""

import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up the env before each test case"""
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up the test env after each test case if needed.
        """
        self.amenity = None

    def test_amenity_attributes(self):
        """
        Test if the Amenity instance has the required attributes.
        """
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_inheritance(self):
        """
        Test if the Amenity instance is an instance of BaseModel.
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity(self):
        """
        Test the Amenity class.
        """
        amenity = Amenity(name='Pool')
        self.assertEqual(amenity.name, 'Pool')


if __name__ == '__main__':
    unittest.main()
