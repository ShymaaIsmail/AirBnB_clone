#!/usr/bin/python3s
import unittest
import pycodestyle
from models.user import User
import inspect
import models.user

class TestSaveUserModel(unittest.TestCase):
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
if __name__ == '__main__':
    unittest.main()
