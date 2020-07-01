#!/usr/bin/python3
from models.base_model import BaseModel
"""Amenity class"""


class Place(BaseModel):
    """Amenity class"""
    def __init__(self):
        """Initialization"""
        self.name = ""
        self.city_id = ""
        self.user_id = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__()
