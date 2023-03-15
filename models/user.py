#!/usr/bin/python3
"""The User class is a subclass of BaseModel."""

import email
from models.base_model import BaseModel


class User(BaseModel):
    """BaseModel has four attributes: email, password, first_name, and last_name."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
