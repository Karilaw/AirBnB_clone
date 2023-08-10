#!/usr/bin/python3
""" A module representing amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class to represent an amenity."""
    name: str = ''
