#!/usr/bin/python3

"""
This module provides unit tests for Inventory class.
"""

import unittest
from models.inventory_transactions import InventoryTransaction


class TestInventoryTransaction(unittest.TestCase):
    """
    Defines test cases for the Inventory class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Inventory class for each test method.
        """
        self.inventory_transaction = InventoryTransaction()

    def test_has_attributes(self):
        """
        Test that object of Inventorytransaction class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.inventory_transaction, "id"))
        self.assertTrue(hasattr(self.inventory_transaction, "created_at"))
        self.assertTrue(hasattr(self.inventory_transaction, "updated_at"))
        self.assertTrue(hasattr(self.inventory_transaction, "category_id"))
        self.assertTrue(hasattr(self.inventory_transaction, "product_id"))
        self.assertTrue(hasattr(self.inventory_transaction, "color_id"))
        self.assertTrue(hasattr(self.inventory_transaction, "warehouse_id"))
        self.assertTrue(hasattr(self.inventory_transaction, "transaction_type"))
        self.assertTrue(hasattr(self.inventory_transaction, "quantity"))
        self.assertTrue(hasattr(self.inventory_transaction, "source"))
        self.assertTrue(hasattr(self.inventory_transaction, "employee_id"))
        self.assertTrue(hasattr(self.inventory_transaction, "save"))
        self.assertTrue(hasattr(self.inventory_transaction, "__repr__"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
