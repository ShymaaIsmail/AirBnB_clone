#!/usr/bin/python3s
import unittest
import pycodestyle
from models.state import State
import inspect
import models.state

class TestSaveStateModel(unittest.TestCase):
    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(State.__doc__, 'no docs for State Class')
        self.assertIsNotNone(models.state.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(State, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(ignore=['E501', 'W503']) 
        module_path = "models/state.py"
        result = style.check_files([module_path])
        self.assertEqual(result.total_errors, 0)
if __name__ == '__main__':
    unittest.main()
