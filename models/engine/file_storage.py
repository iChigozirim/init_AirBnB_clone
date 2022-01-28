#!/usr/bin/python3
"""Defines a class FileStorage."""
import json
from os.path import exists


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON
    file to instance.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __object."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __object to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file, ensure_ascii=False)

    def reload(self):
        """Deserializes JSON file __file_path to __objects, if it exists."""
        if exists(self.__file_path) is True:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)

