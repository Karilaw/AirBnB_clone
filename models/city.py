#!/usr/bin/python3
"""
a module representing city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class to represent a city."""
    state_id: str = ''
    name: str = ''
