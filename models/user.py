#!/usr/bin/python3
"""Write a class User that inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Initialize user class instance of basemodel class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
