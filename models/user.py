#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    def __init__(self):
        """Init func"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__()
