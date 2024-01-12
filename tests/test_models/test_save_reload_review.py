#!/usr/bin/python3s
import unittest
import pycodestyle
from models.review import Review
import inspect
import models.review

class TestSaveReviewModel(unittest.TestCase):
    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(Review.__doc__, 'no docs for Review Class')
        self.assertIsNotNone(models.review.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(Review, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/review.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)
if __name__ == '__main__':
    unittest.main()
