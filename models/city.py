#!/usr/bin/python3
from models.base_model import BaseModel
"""City class"""


class City(BaseModel):
    """City class"""
    name = ""
    state_id = ""

    def __init__(self):
        """Initialization"""
        super().__init__()
