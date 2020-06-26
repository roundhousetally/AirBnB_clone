#!/usr/bin/python3
""" unit tests for base class """


import unittest
import json
import sys
import pep8
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ test cases for base class """
    def test_id(self):
        """ test ids """
