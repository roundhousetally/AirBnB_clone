#!/usr/bin/python3
""" unit tests for base class """


import unittest
import datetime
import uuid
import json
import os
import pep8
import models
from models.amenity import Amenity
from models import storage


class TestUser(unittest.TestCase):
    """ test cases for user class """
    def test_pep8_user_model(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

    @classmethod
    def setUp(self):
        """ setup amenity """
        self.newtest = Amenity()

    def test_instance(self):
        """ checks if it is an instance of BaseModel"""
        self.assertIsInstance(self.newtest, Amenity)

    def test_no_arg(self):
        """ no arg """
        self.assertEqual(Amenity, type(Amenity()))


if __name__ == "__main__":
        unittest.main()
