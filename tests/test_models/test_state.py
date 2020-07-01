#!/usr/bin/python3
""" unit tests for state class """


import unittest
import datetime
import uuid
import json
import os
import pep8
import models
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """ test cases for state class """
    def test_pep8_state(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/state.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

    @classmethod
    def setUp(self):
        """ setup state """
        self.newtest = State()

    def test_instance(self):
        """ checks if it is an instance of BaseModel"""
        self.assertIsInstance(self.newtest, State)

    def test_no_arg(self):
        """ no arg """
        self.assertEqual(State, type(State()))


if __name__ == "__main__":
        unittest.main()
