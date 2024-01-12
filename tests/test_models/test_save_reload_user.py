#!/usr/bin/python3s
import unittest
import pycodestyle
from models.user import User
import inspect
import models.user
import time
from datetime import datetime, timedelta


class TestSaveUserModel(unittest.TestCase):


    def setUp(self):
        self.new_user = User()

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(User.__doc__, 'no docs for User Class')
        self.assertIsNotNone(models.user.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(User, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")


    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/user.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)

    def test_init_user(self):
        self.assertIsInstance(self.new_user.created_at, datetime)
        self.assertIsInstance(self.new_user.updated_at, datetime)
        self.assertEqual(self.new_user.created_at, self.new_user.updated_at)
        self.assertAlmostEqual(self.new_user.created_at, datetime.now(),
                               delta=timedelta(seconds=(10)))

    def test_save_user(self):
        """Test save """
        new_user = User()
        old_update_at = new_user.updated_at
        old_created_at = new_user.created_at
        time.sleep(1)
        new_user.save()
        self.assertTrue((new_user.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_user.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        self.new_user.name = "test_to_dict"
        actual_dict = self.new_user.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "User")
        self.assertEqual(actual_dict["id"], self.new_user.id)
        self.assertEqual(actual_dict["name"], self.new_user.name)
        self.assertEqual(actual_dict["name"], "test_to_dict")

if __name__ == '__main__':
    unittest.main()
