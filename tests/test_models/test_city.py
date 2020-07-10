#!/usr/bin/python3
""" unit tests for city class """


import unittest
import datetime
import uuid
import json
import os
import pep8
import models
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """ test cases for user class """
    def test_pep8_city_model(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/city.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

    @classmethod
    def setUp(self):
        """ setup city """
        self.newtest = City()

    def test_instance(self):
        """ checks if it is an instance of City """
        self.assertIsInstance(self.newtest, City)

    def test_no_arg(self):
        """ no arg """
        self.assertEqual(City, type(City()))


if __name__ == "__main__":
        unittest.main()
