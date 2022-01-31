#!/usr/bin/python3
"""Defines a class FileStorage."""
import json
from models.base_model import BaseModel
from os.path import exists


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON
    file to instance.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __object."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __object to the JSON file (path: __file_path)."""
        dictionary = {}
        for key in self.__objects:
            dictionary[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary, f, ensure_ascii=False)

    def reload(self):
        """Deserializes JSON file __file_path to __objects, if it exists."""
        if exists(self.__file_path) is True:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    dictionary = eval(value["__class__"])(**value)
                    self.__objects[key] = dictionary
