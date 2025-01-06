#!/usr/bin/python3

"""
This module provides unit tests for Supplier class
"""

from models.suppliers import Supplier
import unittest


class TestSupplier(unittest.TestCase):
    """
    Defines test cases for the Supplier class attributes and methods
    """
    def setUp(self):
        """ Instantiates the Supplier class for each test methods """
        self.supplier = Supplier()
    
    def test_has_attributes(self):
        """
        Test that object of Supplier class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.supplier, "id"))
        self.assertTrue(hasattr(self.supplier, "created_at"))
        self.assertTrue(hasattr(self.supplier, "updated_at"))
        self.assertTrue(hasattr(self.supplier, "company_name"))
        self.assertTrue(hasattr(self.supplier, "phone_number"))
        self.assertTrue(hasattr(self.supplier, "email"))
        self.assertTrue(hasattr(self.supplier, "city"))
        self.assertTrue(hasattr(self.supplier, "state"))
        self.assertTrue(hasattr(self.supplier, "country"))
        self.assertTrue(hasattr(self.supplier, "save"))
        self.assertTrue(hasattr(self.supplier, "__repr__"))

    def test_create_obj_with_kwargs(self):
        """ 
        Test that objects of Supplier class can be created
        with keyword arguments
        """
        supplier = Supplier(company_name="WH1", street="glory street",
                              city="LeftRight", state="Double"
                            )
        self.assertEqual(supplier.company_name, "WH1")
        self.assertEqual(supplier.street, "glory street")
        self.assertEqual(supplier.city, "LeftRight")
        self.assertEqual(supplier.state, "Double")

