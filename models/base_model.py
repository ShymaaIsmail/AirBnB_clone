#!/usr/bin/python3
import uuid
from datetime import datetime

"""
This is a class BaseModel that defines all common
attributes/methods for other classes:
"""


class BaseModel:
    """class BaseModel Definition"""
    def __init__(self, *args, **kwargs):
        """initialize the instance attributes values"""
        if kwargs:
            self.kwargs_init(**kwargs)
        else:
            self.default_init()
            from models import storage
            storage.new(self.to_dict())

    def default_init(self):
        """Initialize instance attributes with default values"""
        self.id = str(uuid.uuid4())
        current_datetime = datetime.now()
        self.created_at = current_datetime
        self.updated_at = current_datetime

    def kwargs_init(self, **kwargs):
        """Initialize instance attributes with kwargs items"""
        for attr_key in kwargs.keys():
            attr_value = kwargs[attr_key]
            if (attr_key != '__class__'):
                if (attr_key in ("created_at", "updated_at")):
                    try:
                        attr_value = datetime.fromisoformat(attr_value)
                    except ValueError:
                        attr_value = datetime.now
                setattr(self, attr_key, attr_value)

    def __str__(self):
        """ It returns human readable format of the instance attributes"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """It saves instance and update updated_at attribute"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts the instance to a dictionary excluding private attributes
            and convert datetime to string
        """
        full_dict = self.__dict__.copy()
        full_dict['__class__'] = self.__class__.__name__
        full_dict['created_at'] = self.created_at.isoformat()
        full_dict['updated_at'] = self.updated_at.isoformat()
        return full_dict
