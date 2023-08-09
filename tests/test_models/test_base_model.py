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

    def test_attribute_assignment(self):
        """Test if the instance allows attribute assignment"""
        obj = BaseModel()
        obj.name = "Mary"
        self.assertTrue(hasattr(obj, 'name'))
        self.assertEqual(obj.name, "Mary")

    def test_attribute_reassignment(self):
        """Test if the instance allows attribute reassignment"""
        obj = BaseModel()
        obj.name = "Mary"
        obj.name = "Janet"
        self.assertEqual(obj.name, "Janet")

    def test_attribute_removal(self):
        """Test if the instance allows attribute removal"""
        obj = BaseModel()
        obj.name = "Janet"
        del obj.name
        self.assertFalse(hasattr(obj, 'name'))

    def test_id_uniqueness(self):
        """Test if the generated IDs are unique."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)


if __name__ == '__main__':
    unittest.main()
