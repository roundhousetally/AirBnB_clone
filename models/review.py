#!/usr/bin/python3
from models.base_model import BaseModel
"""Review class"""


class Review(BaseModel):
    """Amenity class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        super().__init__()
