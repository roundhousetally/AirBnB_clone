#!/usr/bin/python3
from models.base_model import BaseModel
"""User class"""


class User(BaseModel):
    """User class"""
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__()
