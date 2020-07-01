#!/usr/bin/python3
""" unit tests for user class """


import unittest
import datetime
import uuid
import json
import os
import pep8
import models
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """ test cases for user class """
    def test_pep8_user_model(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/user.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

    @classmethod
    def setUp(self):
        """ setup user """
        self.newtest = User()

    def test_instance(self):
        """ checks if it is an instance of User"""
        self.assertIsInstance(self.newtest, User)

    def test_no_arg(self):
        """ no arg """
        self.assertEqual(User, type(User()))


if __name__ == "__main__":
        unittest.main()
