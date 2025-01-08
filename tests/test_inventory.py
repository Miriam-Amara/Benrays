#!/usr/bin/python3

"""
This module provides unit tests for Inventory class.
"""

import unittest
from models.inventory import Inventory
from models.products import Category, Product, Color
from models.warehouses import Warehouse


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
        self.assertTrue(hasattr(self.inventory, "__str__"))

    def test_save(self):
        """ Confirms objects are saved to database """
        category = Category(name="peoei")
        product = Product(name="kdiej", category_id=category.id)
        color = Color(name="74673")
        warehouse = Warehouse(name="WH3", phone_number="0958574",
                               street="aaa", city="aaaa", state="aaaa"
                            )
        inventory = Inventory(category_id=category.id, product_id=product.id,
                              color_id=color.id, quantity=5000, warehouse_id=warehouse.id,
                            )
        
        category.save()
        product.save()
        color.save()
        warehouse.save()
        inventory.save()


if __name__ == "__main__":
    unittest.main(verbosity=2)
