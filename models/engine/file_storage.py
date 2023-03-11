#!/usr/bin/python3
"""Type module FileStorage"""

import os.path
import json
from models.base_model import BaseModel


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
        """Type method reaload"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_d = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_d)(**obj))
            return
