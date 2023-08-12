#!/usr/bin/python3
"""
Unit tests for the Place class.
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def setUp(self):
        """Set up the environment before each test case."""
        self.place = Place()

    def tearDown(self):
        """Clean up the environment after each test case if needed."""
        self.place = None

    def test_place_attributes(self):
        """Test if the Place instance has the required attributes."""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_place_inheritance(self):
        """Test if the Place instance is an instance of BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_place(self):
        """Test the Place class."""
        place = Place(
            city_id='SF',
            user_id='123',
            name='Golden Gate Park',
            description='A large urban park',
            number_rooms=0,
            number_bathrooms=0,
            max_guest=0,
            price_by_night=0,
            latitude=37.7694,
            longitude=-122.4862,
            amenity_ids=[]
        )
        self.assertEqual(place.city_id, 'SF')
        self.assertEqual(place.user_id, '123')
        self.assertEqual(place.name, 'Golden Gate Park')
        self.assertEqual(place.description, 'A large urban park')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 37.7694)
        self.assertEqual(place.longitude, -122.4862)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
