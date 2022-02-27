#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""
import models
import unittest
import os
from time import sleep
from datetime import date, datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of BaseModel class."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_one_model_id(self):
        obj = BaseModel()
        self.assertTrue(obj.id)

    def test_two_models_unique_ids(self):
        obj_0 = BaseModel()
        obj_1 = BaseModel()
        self.assertNotEqual(obj_0.id, obj_1.id)

    def test_two_models_varing_created_at(self):
        obj_1 = BaseModel()
        sleep(0.5)
        obj_2 = BaseModel()
        self.assertLess(obj_1.created_at, obj_2.created_at)

    def test_two_models_varing_updated_at(self):
        obj_1 = BaseModel()
        sleep(0.5)
        obj_2 = BaseModel()
        self.assertLess(obj_1.updated_at, obj_2.updated_at)

    def test_str_representation(self):
        dt = datetime.utcnow()
        dt_repr = repr(dt)
        obj = BaseModel()
        obj.id = "1234567"
        obj.created_at = obj.updated_at = dt
        obj_str = obj.__str__()
        self.assertIn("[BaseModel] (1234567)", obj_str)
        self.assertIn("'id': '1234567'", obj_str)
        self.assertIn("'created_at': " + dt_repr, obj_str)
        self.assertIn("'updated_at': " + dt_repr, obj_str)

    def test_args_unused(self):
        obj = BaseModel('1234')
        self.assertNotIn('1234', obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.utcnow()
        dt_iso = dt.isoformat()
        obj = BaseModel(id="543", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj.id, "543")
        self.assertEqual(obj.created_at, dt)
        self.assertEqual(obj.updated_at, dt)

    
class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

        
    def test_one_save(self):
        obj = BaseModel()
        sleep(0.5)
        first_updated_at = obj.updated_at
        obj.save()
        self.assertLess(first_updated_at, obj.updated_at)

    def test_save_with_arg(self):
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save("")

    def test_save_updates_file(self):
       obj = BaseModel()
       obj.save()
       obj_id = "BaseModel." + obj.id
       with open("file.json", "r") as f:
           self.assertIn(obj_id, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the BaseMethod class."""

    def test_to_dict_type(self):
        obj = BaseModel()
        self.assertTrue(dict, type(obj.to_dict()))

    def test_to_dict_elements(self):
        dt = datetime.utcnow()
        obj = BaseModel()
        obj.id = "12345"
        obj.created_at = obj.updated_at = dt
        obj.name = "Betty"
        obj.number = 89
        to_dict = {
            'id': "12345",
            '__class__': 'BaseModel',
            'name': 'Betty',
            'number': 89,
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(to_dict, obj.to_dict())
        
    def test_to_dict_with_arg(self):
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.to_dict("")
        

if __name__ == "__main__":
    unittest.main()