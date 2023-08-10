#!/usr/bin/python3
"""A state module representing
state attributes and methods
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class to represent a state."""
    name: str = ''
