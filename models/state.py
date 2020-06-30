#!/usr/bin/python3
from models.base_model import BaseModel
"""User class"""


class State(BaseModel):
    """User class"""
    def __init__(self):
        """Initialization"""
        self.name = ""
        super().__init__()
