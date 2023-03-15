#!/usr/bin/python3
"""Write a class User that inherits from BaseModel."""
from models.base_model import BaseModel


class user(BaseModel):
    """User class is a subclass of the BaseModel class."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
