#!/usr/bin/python3
""" A module to test base class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization of BaseModel instance"""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    def test_str(self):
        """Test string representation of BaseModel instance"""
        b = BaseModel()
        expected = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(str(b), expected)

    def test_save(self):
        """Test save method of BaseModel instance"""
        b = BaseModel()
        old_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(old_updated_at, b.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel instance"""
        b = BaseModel()
        d = b.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
