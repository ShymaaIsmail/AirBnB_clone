#!/usr/bin/python3s
import unittest
import pycodestyle
from models.city import City
import inspect
import models.city
import time
from datetime import datetime, timedelta

class TestSaveCityModel(unittest.TestCase):

    def setUp(self):
        self.new_city = City()

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(City.__doc__, 'no docs for City Class')
        self.assertIsNotNone(models.city.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(City, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/city.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)


    
    def test_init_city(self):
        self.assertIsInstance(self.new_city.created_at, datetime)
        self.assertIsInstance(self.new_city.updated_at, datetime)
        self.assertEqual(self.new_city.created_at, self.new_city.updated_at)
        self.assertAlmostEqual(self.new_city.created_at, datetime.now(),
                               delta=timedelta(seconds=(10)))

    def test_save_city(self):
        """Test save """
        new_city = City()
        old_update_at = new_city.updated_at
        old_created_at = new_city.created_at
        time.sleep(1)
        new_city.save()
        self.assertTrue((new_city.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_city.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        self.new_city.name = "test_to_dict"
        actual_dict = self.new_city.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "City")
        self.assertEqual(actual_dict["id"], self.new_city.id)
        self.assertEqual(actual_dict["name"], self.new_city.name)
        self.assertEqual(actual_dict["name"], "test_to_dict")

if __name__ == '__main__':
    unittest.main()
