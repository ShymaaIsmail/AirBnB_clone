#!/usr/bin/python3
import json
import os
""" File Storage Module"""


class FileStorage:
    """File Storage Class Definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns All Stored Objects"""
        return self.__objects

    def new(self, obj):
        """Set obj with its key in __objects"""
        if obj:
            class_name = obj["__class__"]
            id = obj["id"]
            self.__objects[f"{class_name}.{id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)
            self.reload()

    def reload(self):
        """Deserializes the JSON file to __objects if __file_path exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    self.__objects = json.load(file)
                except:
                    self.__objects = {}
