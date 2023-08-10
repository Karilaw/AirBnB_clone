#!/usr/bin/python3
"""A module that represents Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class to represent a review."""
    place_id: str = ''
    user_id: str = ''
    text: str = ''
