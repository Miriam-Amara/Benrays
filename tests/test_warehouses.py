#!/usr/bin/python3

"""
This module provides unit tests for Warehouse class
"""

from models.warehouses import Warehouse
import unittest


class TestWarehouse(unittest.TestCase):
    """
    Defines test cases for the Warehouse class attributes and methods
    """
    def setUp(self):
        """ Instantiates the Warehouse class for each test methods """
        self.warehouse = Warehouse()
    
    def test_has_attributes(self):
        """
        Test that object of Warehouse class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.warehouse, "id"))
        self.assertTrue(hasattr(self.warehouse, "created_at"))
        self.assertTrue(hasattr(self.warehouse, "updated_at"))
        self.assertTrue(hasattr(self.warehouse, "name"))
        self.assertTrue(hasattr(self.warehouse, "phone_number"))
        self.assertTrue(hasattr(self.warehouse, "street"))
        self.assertTrue(hasattr(self.warehouse, "city"))
        self.assertTrue(hasattr(self.warehouse, "state"))
        self.assertTrue(hasattr(self.warehouse, "save"))
        self.assertTrue(hasattr(self.warehouse, "__repr__"))

    def test_create_obj_with_kwargs(self):
        """ 
        Test that objects of Warehouse class can be created
        with keyword arguments
        """
        warehouse = Warehouse(name="WH1", street="glory street",
                              city="LeftRight", state="Double"
                            )
        self.assertEqual(warehouse.name, "WH1")
        self.assertEqual(warehouse.street, "glory street")
        self.assertEqual(warehouse.city, "LeftRight")
        self.assertEqual(warehouse.state, "Double")

