#!/usr/bin/python3
""" unit tests for base class """


import unittest
import datetime
import uuid
import json
import os
import pep8
import models
from models.base_model import BaseModel
from models import storage
BaseModel = models.base_model.BaseModel


class TestBase(unittest.TestCase):
    """ test cases for base class """
    def test_pep8_base_model(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

    @classmethod
    def setUp(self):
        """ setup basemodel """
        self.newtest = BaseModel()

    def test_instance(self):
        """ checks if it is an instance of BaseModel"""
        self.assertIsInstance(self.newtest, BaseModel)

    def test_no_arg(self):
        """ no arg """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_save(self):
        """ save method """
        Bm = BaseModel()
        Bm.name = "Tahlia"
        Bm.save()
        self.assertEqual(Bm.name, "Tahlia")

    def test_todict(self):
        """ dict method """
        time = datetime.datetime.now()
        bm = BaseModel()
        bm.id = "7"
        bm.created_at = bm.updated_at = time
        newdict = {
            "id": "7",
            "created_at": time.isoformat(),
            "updated_at": time.isoformat(),
            "__class__": "BaseModel"
        }
        self.assertDictEqual(bm.to_dict(), newdict)

    def test_attrtypes(self):
        """ attribute types """

if __name__ == "__main__":
        unittest.main()
