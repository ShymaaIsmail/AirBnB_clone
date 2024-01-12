#!/usr/bin/python3
"""Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_it = ""
    user_id = ""
    text = ""
