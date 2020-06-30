#!/usr/bin/python3
""" unit tests for base class """


import unittest
import json
import sys
import pep8
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ test cases for base class """
    @classmethod
    def setUpClass(cls):
        """ sets up an instance to test """
        cls.newtest = BaseModel()

    @classmethod
    def teardown(cls):
        """ deletes the instance """
        
    def test_id(self):
        """ test that id is str """
        self.assertEqual(str, type(self.inst.id
