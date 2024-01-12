#!/usr/bin/python3s
import unittest
import pycodestyle
from models.amenity import Amenity
import inspect
import models.amenity
import time
from datetime import datetime, timedelta
class TestSaveReloadAmenityModel(unittest.TestCase):

    def setUp(self):
        self.new_amenity = Amenity()

    def tearDown(self):
        pass

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(Amenity.__doc__, 'no docs for Amenity Class')
        self.assertIsNotNone(models.amenity.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(Amenity, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/amenity.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)

    def test_init_amenity(self):
        self.assertIsInstance(self.new_amenity.created_at, datetime)
        self.assertIsInstance(self.new_amenity.updated_at, datetime)
        self.assertEqual(self.new_amenity.created_at, self.new_amenity.updated_at)
        self.assertAlmostEqual(self.new_amenity.created_at, datetime.now(),
                               delta=timedelta(seconds=(10)))


    def test_save(self):
        """Test save """
        new_amenity = Amenity()
        old_update_at = new_amenity.updated_at
        old_created_at = new_amenity.created_at
        time.sleep(1)
        new_amenity.save()
        self.assertTrue((new_amenity.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_amenity.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        self.new_amenity.name = "test_to_dict"
        actual_dict = self.new_amenity.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "Amenity")
        self.assertEqual(actual_dict["id"], self.new_amenity.id)
        self.assertEqual(actual_dict["name"], self.new_amenity.name)
        self.assertEqual(actual_dict["name"], "test_to_dict")

if __name__ == '__main__':
    unittest.main()
