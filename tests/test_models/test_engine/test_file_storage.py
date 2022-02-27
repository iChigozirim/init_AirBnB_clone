#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import os
import json
from statistics import mode
from typing import Reversible
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage("")

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittest for testing methods in the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass
    
    @classmethod
    def tearDown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(type(models.storage.all()), dict)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all("")

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        ct = City()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(pl)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + bm.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + bm.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("City." + bm.id, models.storage.all().keys())
        self.assertIn(ct, models.storage.all().values())
        self.assertIn("Amenity." + bm.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Place." + bm.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("Review." + bm.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(User(), State())

    def test_new_with_no_arg(self):
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        ct = City()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(pl)
        models.storage.new(rv)
        with open("file.json", "r") as f:
            json_text = f.read()
            self.assertIn("BaseModel." + bm.id, json_text)
            self.assertIn("User." + us.id, json_text)
            self.assertIn("State." + st.id, json_text)
            self.assertIn("City." + ct.id, json_text)
            self.assertIn("Amenity." + am.id, json_text)
            self.assertIn("Place." + pl.id, json_text)
            self.assertIn("Review." + rv.id, json_text)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save("")

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        ct = City()
        am = Amenity()
        pl = Place()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("City." + ct.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload("")

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())
    
    
if __name__ == "__main__":
    unittest.main()