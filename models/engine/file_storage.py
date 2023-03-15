#!/usr/bin/python3
"""Type module FileStorage"""

import json

from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """Type class File Storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Type method all"""
        return FileStorage.__objects

    def new(self, obj):
        """Type method new"""
        F_objdict = FileStorage.__objects
        object_name = obj.__class__.__name__
        F_objdict["{}.{}".format(object_name, obj.id)] = obj

    def save(self):
        """Type method save"""
        F_objdict = FileStorage.__objects
        obj_dict = {obj: F_objdict[obj].to_dict() for obj in F_objdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f, indent=2)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                obj_dir = json.loads(f.read())
                for key, value in obj_dir.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass
