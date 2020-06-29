#!/usr/bin/python3
import uuid
from datetime import datetime
import models
import models.engine
"""The module contains the models in the hBnB clone"""


class BaseModel():
    """This class is the bass for all hbnb objects"""

    def __init__(self, *args, **kwargs):
        """Init func"""
        tf = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at':
                    v = datetime.strptime(v, tf)
                if k == 'updated_at':
                    v = datetime.strptime(v, tf)
                if k == '__class__':
                    v = self.__class__
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """STRRRRRRRRR"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Save me"""
        from models import storage
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """returns dict obj with class name"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.update(__class__=self.__class__.__name__)
        return my_dict
