#!/usr/bin/python3
"""The `Review` class inherits from the `BaseModel` class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Creating a public class attribute."""

    place_id = ""
    user_id = ""
    text = ""
