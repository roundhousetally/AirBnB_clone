#!/usr/bin/python3
from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """User class"""
    def __init__(self):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()
