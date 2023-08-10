#!/usr/bin/python3
"""A model that defines user and all its
attributes and methods"""


from models.base_model import BaseModel

class User(BaseModel):
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''

