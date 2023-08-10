#!/usr/bin/python3
"""A module to test various classes
"""


import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestModels(unittest.TestCase):
    """A class to test the models."""

    def test_state(self):
        """Test the State class."""
        state = State(name='California')
        self.assertEqual(state.name, 'California')

    def test_city(self):
        """Test the City class."""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.state_id, 'CA')
        self.assertEqual(city.name, 'San Francisco')

    def test_amenity(self):
        """Test the Amenity class."""
        amenity = Amenity(name='Pool')
        self.assertEqual(amenity.name, 'Pool')

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

    def test_review(self):
        """Test the Review class."""
        review = Review(place_id='GGP', user_id='123', text='Great park!')
        self.assertEqual(review.place_id, 'GGP')
        self.assertEqual(review.user_id, '123')
        self.assertEqual(review.text, 'Great park!')


if __name__ == '__main__':
    unittest.main()
