#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel

class City(BaseModel):
    '''
        This is city class implementation
    '''
    state_id = ""
    name = ""
