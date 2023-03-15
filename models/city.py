#!/usr/bin/python3
"""The `City` class inherits from the `BaseModel` class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Creating a public class attribute called name."""

    state_id = ""
    name = ""
