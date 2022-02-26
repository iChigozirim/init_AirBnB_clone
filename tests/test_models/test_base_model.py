#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""
import models
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of BaseModel class."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_one_model_id(self):
        obj = BaseModel()
        self.assertTrue(obj.id)

    def test_two_models_unique_ids(self):
        obj_0 = BaseModel()
        obj_1 = BaseModel()
        self.assertNotEqual(obj_0.id, obj_1.id)

    def test_created_at(self):
        obj = BaseModel()
        self.assertEqual(obj.created_at, datetime.utcnow)

    def test_updated_at(self):
        obj = BaseModel()
        created = obj.created_at
        obj.save()
        self.assertNotEqual(created, obj.updated_at)