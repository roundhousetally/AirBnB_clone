#!/usr/bin/python3
""" File Storage """
from models.base_model import BaseModel
from os import path
import json


class FileStorage():
    """ file store """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dict objs """
        return FileStorage.__objects

    def new(self, obj):
        """ sets obj with key """
        keyval = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[keyval] = obj.to_dict()

    def save(self):
        """ serializes obj """
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ deserializes obj """
        from models.base_model import BaseModel

        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r+', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
