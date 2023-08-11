#!/usr/bin/python3
""" A module to test base class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    """Test casess for BaseModel class""""""Test casess for BaseModel class"""

    def setUp(self):
        """Set up the env before each test case"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up the test env after each test case if needed"""
        pass

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

    def test_created_at_after_init(self):
        """Test if created_at is set correctly at initialization"""
        now = datetime.now()
        obj = BaseModel()
        time_difference = now - obj.created_at
        self.assertLessEqual(time_difference, timedelta(seconds=1))

    def test_updated_at_after_init(self):
        """Test if updated_at is set correctly at initialization"""
        now = datetime.now()
        obj = BaseModel()
        time_difference = now - obj.updated_at
        self.assertLessEqual(time_difference, timedelta(seconds=2))

    def test_save_updates_updated_at(self):
        """Test if save method updates updated_at"""
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)

    def test_to_dict_structure(self):
        """Test the structure of the dictionary returned by to_dict"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_values(self):
        """Test the values of the dictionary returned by to_dict"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
