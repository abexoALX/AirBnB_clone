#!/usr/bin/python3

'''
    All the test for the review model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''

    def setUp(self):
        '''
            Creates an instance for Review.
        '''
        self.new_review = Review()

    def test_Review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_review, BaseModel)

    def test_Review_attributes(self):
        '''
            Checks that the attribute exist.
        '''
        self.assertTrue("place_id" in self.new_review.__dir__())
        self.assertTrue("user_id" in self.new_review.__dir__())
        self.assertTrue("text" in self.new_review.__dir__())

    def test_type_place_id(self):
        '''
            Test the type of user_id.
        '''
        place_id = getattr(self.new_review, "place_id")
        self.assertIsInstance(place_id, str)

    def test_type_user_id(self):
        '''
            Test the type of user_id.
        '''
        user_id = getattr(self.new_review, "user_id")
        self.assertIsInstance(user_id, str)

    def test_type_text_id(self):
        '''
            Test the type of text.
        '''
        text = getattr(self.new_review, "text")
        self.assertIsInstance(text, str)
