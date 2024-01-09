#!/usr/bin/python3s
import unittest
import uuid
import time
from datetime import datetime, timedelta

from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):

    def test_default(self):
        """ sample test case in the project"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    def test_initialization_id(self):
        """Test BaseModel id initialization"""
        new_model = BaseModel()
        self.assertIsInstance(new_model.id, str)
        try:
            self.assertIsInstance(uuid.UUID(new_model.id), uuid.UUID)
        except Exception as e:
            self.fail("id attribute is not a valid UUID")

    def test_initialization_dates(self):
        """Test BaseModel dates initialization"""
        new_model = BaseModel()
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
        self.assertEqual(new_model.created_at, new_model.updated_at)
        self.assertAlmostEqual(new_model.created_at, datetime.now(), delta= timedelta(seconds=(10)))

    def test_str(self):
        """Test str format"""
        model = BaseModel()
        actual_format = str(model)
        expected_format= "[BaseModel] ({}) {}".format(model.id,
                                    model.__dict__)
        self.assertEqual(actual_format, expected_format)

    def test_save(self):
        """Test save """
        new_model = BaseModel()
        old_update_at = new_model.updated_at
        old_created_at = new_model.created_at
        time.sleep(2)
        new_model.save()
        self.assertTrue((new_model.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_model.created_at)

    def test_to_dict(self):
        """Test to dict format"""
        new_model = BaseModel()
        actual_dict = new_model.to_dict()        
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "BaseModel")
        self.assertEqual(actual_dict["id"], new_model.id)
        self.assertEqual(actual_dict["created_at"], new_model.created_at)
        self.assertEqual(actual_dict["updated_at"], new_model.updated_at)

if __name__ == '__main__':
    unittest.main()
