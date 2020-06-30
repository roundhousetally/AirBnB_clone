#!/usr/bin/python3
from models.base_model import BaseModel
"""Review class"""


class Review(BaseModel):
    """Amenity class"""
    def __init__(self):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__()
