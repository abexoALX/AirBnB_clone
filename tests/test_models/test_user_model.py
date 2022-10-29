#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attribute(self):
        '''

            test that the user class attribute exsists
        '''
        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_type_email(self):
        '''
            Test the type of email
        '''
        new_user = User()
        email=getattr(new_user,"email")
        self.assertIsInstance(email, str)

    def test_type_first_name(self):
        '''
            Test the type of first name
        '''
        new_user = User()
        first_name=getattr(new_user,"first_name")
        self.assertIsInstance(first_name, str)

    def test_type_last_name(self):
        '''
            Test the type of last name
        '''
        new_user = User()
        last_name=getattr(new_user,"last_name")
        self.assertIsInstance(last_name, str)

    def test_type_password(self):
        '''
            Test the type of password
        '''
        new_user = User()
        password=getattr(new_user,"last_name")
        self.assertIsInstance(password, str)
