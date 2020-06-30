#!/usr/bin/python3
from models.base_model import BaseModel
"""City class"""


class City(BaseModel):
    """City class"""
    def __init__(self):
        """Initialization"""
        self.name = ""
        self.state_id = ""
        super().__init__()
