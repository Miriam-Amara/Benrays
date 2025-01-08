#!/usr/bin/python3

"""
This module contains unit tests for BaseModel class
"""


import unittest
import os
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ 
    Contains test cases for attributes and methods
    of BaseModel class
    """

    def setUp(self):
        """ 
        Creates an instace of BaseModel class
        for each test_ methods.
        """
        self.basemodel = BaseModel()
    
    def test_has_instance_attributes(self):
        """ 
        Confirms the required instance attributes are
        present in the BaseModel class.
        """
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.assertIsInstance(self.basemodel.id, str)
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertIsInstance(self.basemodel.created_at, datetime)
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertTrue(hasattr(self.basemodel, "save"))
        self.assertTrue(hasattr(self.basemodel, "__str__"))

    def test_has_class_attributes(self):
        """ 
        Confirms the required class attributes are
        present in the BaseModel class.
        """
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "created_at"))
        self.assertTrue(hasattr(BaseModel, "updated_at"))

    def test_create_objects_with_kwargs(self):
        """
        Tests BaseModel objects can be created with
        keyword arguments.
        """
        basemodel = BaseModel(name="Togo", age=35)
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertTrue(hasattr(basemodel, "age"))

    def test_recreate_obj(self):
        basemodel = BaseModel(name="Market", year=2019)
        new_basemodel = BaseModel(**basemodel.__dict__)
        self.assertEqual(basemodel.id, new_basemodel.id)
        self.assertEqual(basemodel.created_at, new_basemodel.created_at)
        self.assertEqual(basemodel.updated_at, new_basemodel.updated_at)
        self.assertEqual(new_basemodel.name, "Market")
        self.assertEqual(new_basemodel.year, 2019)

    def test_repr(self):
        """
        Tests that __repr__() returns an unambiguous string representation
        of the object for debugging and logging.
        """
        # result = (
        #     f"{self.basemodel.__class__.__name__}(id={self.basemodel.id}, "
        #     f"created_at={self.basemodel.created_at}, "
        #     f"updated_at={self.basemodel.updated_at})"
        # )
        # self.assertEqual(result, self.basemodel.__repr__())

    def test_save(self):
        """
        Confirms that obj updated_at attribute
        records the time an update is made to the object.
        """
        if os.getenv("DB_ENV") != "test":
            previous_value = self.basemodel.updated_at
            self.basemodel.save()
            current_value = self.basemodel.updated_at
            self.assertGreater(current_value, previous_value)

    def test_to_dict(self):
        """ 
        Confirms that a dictionary representation of the object
        is returned.
        """
        obj_dict = self.basemodel.to_dict()
        self.assertIn("__class__", obj_dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
