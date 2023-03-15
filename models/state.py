#!/usr/bin/python3
"""The `State` class inherits from the
 `BaseModel` class, and has a `name` attribute."""
from models.base_model import BaseModel


class State(BaseModel):
    """Creating a public class attribute called name."""

    name = ""
