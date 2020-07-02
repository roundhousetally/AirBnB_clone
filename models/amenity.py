#!/usr/bin/python3
from models.base_model import BaseModel
"""Amenity class"""


class Amenity(BaseModel):
    """Amenity class"""
    name = ""
    def __init__(self):
        super().__init__()
