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
        FileStorage.__objects[keyval] = obj

    def save(self):
        """ serializes obj """
        import models
        newdict = {}
        for key, value in FileStorage.__objects.items():
            newdict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as f:
            json.dump(newdict, f)

    def reload(self):
        """ deserializes object """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                tempdict_objs = json.load(f)
            for key, value in tempdict_objs.items():
                obj = eval(value['__class__'])(**value)
                FileStorage.__objects[key] = obj
        except:
            pass
