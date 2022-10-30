#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''

    def setUp(self):
        '''
            Creates an instance for Amenity.
        '''
        self.new_amenity = Amenity()


    def test_Amenity_inheritance(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_amenity, BaseModel)


    def test_Amenity_attributes(self):
        '''
            Checks that the attribute exist.
        '''
        self.assertTrue("name" in self.new_amenity.__dir__())

    def test_type_name(self):
        '''
            Test the type of name.
        '''
        name = getattr(self.new_amenity, "longitude")
        self.assertIsInstance(name, str)


