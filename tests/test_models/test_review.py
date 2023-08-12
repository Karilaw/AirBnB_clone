#!/usr/bin/env python3
"""
Unit tests for the Review class.
"""


import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up the environment before each test case."""
        self.review = Review()

    def tearDown(self):
        """Clean up the environment after each test case if needed."""
        self.review = None

    def test_review_attributes(self):
        """Test if the Review instance has the required attributes."""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_inheritance(self):
        """Test if the Review instance is an instance of BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_review(self):
        """Test the Review class."""
        review = Review(
            place_id='place123',
            user_id='user456',
            text='Great place to stay!'
        )
        self.assertEqual(review.place_id, 'place123')
        self.assertEqual(review.user_id, 'user456')
        self.assertEqual(review.text, 'Great place to stay!')


if __name__ == '__main__':
    unittest.main()
