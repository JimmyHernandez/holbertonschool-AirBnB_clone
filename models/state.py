#!/usr/bin/python3
"""Test class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Creating a public class attribute called name."""

    state_id = ""
    name = ""
