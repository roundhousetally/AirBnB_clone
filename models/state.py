#!/usr/bin/python3
from models.base_model import BaseModel
"""User class"""


class State(BaseModel):
    """User class"""
    name = ""
    def __init__(self):
        """Initialization"""
        super().__init__()
