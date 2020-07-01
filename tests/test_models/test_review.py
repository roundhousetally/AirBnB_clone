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


class TestReview(unittest.TestCase):
    """ test cases for review class """
    def test_pep8_review(self):
        """ tests pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        errs = pep8style.check_files(['models/review.py'])
        self.assertEqual(errs.total_errors, 0, errs.messages)

    @classmethod
    def setUp(self):
        """ setup user """
        self.newtest = Review()

    def test_instance(self):
        """ checks if it is an instance of review"""
        self.assertIsInstance(self.newtest, Review)

    def test_no_arg(self):
        """ no arg """
        self.assertEqual(Review, type(Review()))


if __name__ == "__main__":
        unittest.main()
