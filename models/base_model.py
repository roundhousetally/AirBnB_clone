#!/usr/bin/python3
import uuid
import datetime
"""The module contains the models in the hBnB clone"""


class BaseModel():
    """This class is the bass for all hbnb objects"""

    def __init__(self):
        """Init func"""
        self.id = str(uuid.uuid4())
        self.created_at = (datetime.datetime.now()).isoformat()
        self.updated_at = (datetime.datetime.now()).isoformat()

    def __str__(self):
        """STRRRRRRRRR"""
        return "[{}] {} {}".format(self.__class__.__name__,
                                   self.id, self.__dict__)

    def save(self):
        """Save me"""
        self.updated_at = (datetime.datetime.now()).isoformat()

    def to_dict(self):
        """returns dict obj with class name"""
        my_dict = self.__dict__
        my_dict.update(__class__=self.__class__.__name__)
        return my_dict
