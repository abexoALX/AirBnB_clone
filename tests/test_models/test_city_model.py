#!/usr/bin/python3

'''
    All the test for the city model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    '''
        Testing City class
    '''

    def setUp(self):
        '''
            Creates an instance for city.
        '''
        self.new_city = City()

    def test_City_inheritance(self):
        '''
            tests that the city class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_city, BaseModel)

    def test_City_attributes(self):
        '''
            Checks that the attribute exist.
        '''
        self.assertTrue("state_id" in self.new_city.__dir__())
        self.assertTrue("name " in self.new_city.__dir__())


    def test_type_state_id(self):
        '''
            Test the type of state id
        '''
        state_id = getattr(self.new_city, "state_id")
        self.assertIsInstance(state_id, str)

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "name")
        self.assertIsInstance(name, str)
