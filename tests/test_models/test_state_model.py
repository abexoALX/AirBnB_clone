#!/usr/bin/python3
'''
    All the test for the state model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.state import State

class TestUser(unittest.TestCase):
    '''
        Testing State class
    '''

    def test_State_inheritance(self):
        '''
            tests that the State class Inherits from BaseModel
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attribute(self):
        '''

            test that the state class attribute exists
        '''
        new_user = State()
        self.assertTrue("name" in new_user.__dir__())

    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_state = State()
        name=getattr(new_state,"email")
        self.assertIsInstance(name, str)
