#!/usr/bin/python3
""" unit tests for review class """


import unittest
import datetime
import uuid
import json
import os
import pep8
import models
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """ test cases for filestorage class """
    def test_pep8_filestorage(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

if __name__ == "__main__":
        unittest.main()
