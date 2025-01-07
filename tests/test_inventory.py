#!/usr/bin/python3

"""
This module provides unit tests for Inventory class.
"""

import unittest
from models.inventory import Inventory


class TestInventory(unittest.TestCase):
    """
    Defines test cases for the Inventory class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Inventory class for each test method.
        """
        self.inventory = Inventory()

    def test_has_attributes(self):
        """
        Test that object of Inventory class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.inventory, "id"))
        self.assertTrue(hasattr(self.inventory, "created_at"))
        self.assertTrue(hasattr(self.inventory, "updated_at"))
        self.assertTrue(hasattr(self.inventory, "category_id"))
        self.assertTrue(hasattr(self.inventory, "product_id"))
        self.assertTrue(hasattr(self.inventory, "color_id"))
        self.assertTrue(hasattr(self.inventory, "quantity"))
        self.assertTrue(hasattr(self.inventory, "warehouse_id"))
        self.assertTrue(hasattr(self.inventory, "save"))
        self.assertTrue(hasattr(self.inventory, "__repr__"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
