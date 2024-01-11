#!/usr/bin/python3s
import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta

class TestBaseModelDict(unittest.TestCase):

    def test_default(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        print(my_model.id)
        print(my_model)
        print(type(my_model.created_at))
        print("--")
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key,
                                           type(my_model_json[key]),
                                           my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.id, my_model.id)


    def test_kwargs(self):
        valid_dict =  {"id": "id-32",
                        "created_at": "2024-01-10T22:40:45.795104",
                        "updated_at": "2024-01-10T22:40:45.795104",
                        "__class__": "abc"}
        actual_model = BaseModel(**valid_dict)
        self.assertEqual(actual_model.id, "id-32")
        self.assertEqual(actual_model.created_at, datetime(2024, 1, 10, 22, 40, 45, 795104))
        self.assertEqual(actual_model.updated_at, datetime(2024, 1, 10, 22, 40, 45, 795104) )
        self.assertEqual(actual_model.to_dict()["__class__"], "BaseModel")

    def test_invalid_kwargs(self):
        invalid_dict =  {"id": "id-32",
                        "created_at": "today",
                        "updated_at": "1111102223",
                        "__class__": "abc"}
        with self.assertRaises(ValueError):
            actual_model = BaseModel(**invalid_dict)

if __name__ == '__main__':
    unittest.main()
