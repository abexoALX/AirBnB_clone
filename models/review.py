#!/usr/bin/python3
'''
    Implementation of the Review class which inherits from BaseModel
'''
from models.base_model import BaseModel

class Review(BaseModel):
    '''
        Review class implementation
    '''
    place_id = ""
    user_id = ""
    text = ""
