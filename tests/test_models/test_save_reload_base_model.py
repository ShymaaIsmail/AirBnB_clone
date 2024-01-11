#!/usr/bin/python3s
import unittest
import os
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestSaveReloadBaseModel(unittest.TestCase):

    def test_default(self):
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)

class TestFileStorageModel(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    
if __name__ == '__main__':
    unittest.main()
