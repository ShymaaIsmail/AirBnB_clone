#!/usr/bin/python3s
import unittest
import pycodestyle
from models.city import City
import inspect
import models.city
class TestSaveCityModel(unittest.TestCase):
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
if __name__ == '__main__':
    unittest.main()
