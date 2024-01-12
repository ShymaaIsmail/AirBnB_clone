#!/usr/bin/python3s
import unittest
import pycodestyle
from models.state import State
import inspect
import models.state
import time
from datetime import datetime, timedelta


class TestSaveStateModel(unittest.TestCase):

    
    def setUp(self):
        self.new_state = State()

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

    def test_init_state(self):
        self.assertIsInstance(self.new_state.created_at, datetime)
        self.assertIsInstance(self.new_state.updated_at, datetime)
        self.assertEqual(self.new_state.created_at, self.new_state.updated_at)
        self.assertAlmostEqual(self.new_state.created_at, datetime.now(),
                               delta=timedelta(seconds=(10)))

    def test_save_state(self):
        """Test save """
        new_state = State()
        old_update_at = new_state.updated_at
        old_created_at = new_state.created_at
        time.sleep(1)
        new_state.save()
        self.assertTrue((new_state.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_state.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        self.new_state.name = "test_to_dict"
        actual_dict = self.new_state.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "State")
        self.assertEqual(actual_dict["id"], self.new_state.id)
        self.assertEqual(actual_dict["name"], self.new_state.name)
        self.assertEqual(actual_dict["name"], "test_to_dict")

if __name__ == '__main__':
    unittest.main()
