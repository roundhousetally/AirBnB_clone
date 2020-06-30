#!/usr/bin/python3
from models.base_model import BaseModel
"""Amenity class"""


class Amenity(BaseModel):
    """Amenity class"""
    def __init__(self):
        self.name = ""
        super().__init__()
