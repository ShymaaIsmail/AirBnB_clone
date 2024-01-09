#!/usr/bin/python3
import uuid
from datetime import datetime

"""
This is a class BaseModel that defines all common
attributes/methods for other classes:
"""


class BaseModel:
    """class BaseModel Definition"""
    def __init__(self):
        """initialize the instance attributes values"""
        self.id = str(uuid.uuid4())
        current_datetime = datetime.now()
        self.created_at = current_datetime
        self.updated_at = current_datetime

    def __str__(self):
        """ It returns human readable format of the instance attributes"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """It saves instance and update updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the instance to a dictionary excluding private attributes
            and convert datetime to string
        """
        full_dict = self.__dict__
        full_dict['__class__'] = self.__class__.__name__
        full_dict['created_at'] = datetime.isoformat(self.created_at)
        full_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return full_dict
