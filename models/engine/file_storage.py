#!/usr/bin/python3
""" File Storage Module"""

import json
import os
""" File Storage Module"""


class FileStorage:
    """File Storage Class Definition"""
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """Returns All Stored Objects"""
        return self.__objects

    def new(self, obj):
        """Set obj with its key in __objects"""
        if obj:
            class_name = obj.__class__
            id = obj.id
            self.__objects[f"{class_name}.{id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()
                       }, file)

    def reload(self):
        """Deserializes the JSON file to __objects if __file_path exists"""
        classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    dict = json.loads(f.read())
                    for value in dict.values():
                        cls = value["__class__"]
                        self.new(eval(cls)(**value))
            except Exception:
                pass
