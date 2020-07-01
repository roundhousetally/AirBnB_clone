#!/usr/bin/python3
""" unit tests for place class """


import unittest
import datetime
import uuid
import json
import os
import pep8
import models
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """ test cases for Place class """
    def test_pep8_user_model(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/place.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

    @classmethod
    def setUp(self):
        """ setup place """
        self.newtest = Place()

    def test_instance(self):
        """ checks if it is an instance of BaseModel"""
        self.assertIsInstance(self.newtest, Place)

    def test_no_arg(self):
        """ no arg """
        self.assertEqual(Place, type(Place()))


if __name__ == "__main__":
        unittest.main()
