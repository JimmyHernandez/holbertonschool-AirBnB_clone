#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """Suite of File Storage Tests."""

    my_model = BaseModel()

    def testClassInstance(self):
        """Check instance."""
        self.assertIsInstance(storage, FileStorage)
