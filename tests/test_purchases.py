#!/usr/bin/python3

"""
This module provides unit tests for Purchase class.
"""

import unittest
from models.purchases import Purchase


class TestPurchase(unittest.TestCase):
    """
    Defines test cases for the Purchase class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Purchase class for each test method.
        """
        self.purchases = Purchase()

    def test_has_attributes(self):
        """
        Test that object of Purchase class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.purchases, "id"))
        self.assertTrue(hasattr(self.purchases, "created_at"))
        self.assertTrue(hasattr(self.purchases, "updated_at"))
        self.assertTrue(hasattr(self.purchases, "category_id"))
        self.assertTrue(hasattr(self.purchases, "product_id"))
        self.assertTrue(hasattr(self.purchases, "color_id"))
        self.assertTrue(hasattr(self.purchases, "quantity"))
        self.assertTrue(hasattr(self.purchases, "unit_cost_price"))
        self.assertTrue(hasattr(self.purchases, "total_price"))
        self.assertTrue(hasattr(self.purchases, "amount_paid"))
        self.assertTrue(hasattr(self.purchases, "supplier_id"))
        self.assertTrue(hasattr(self.purchases, "warehouse_id"))
        self.assertTrue(hasattr(self.purchases, "payment_status"))
        self.assertTrue(hasattr(self.purchases, "payment_type"))
        self.assertTrue(hasattr(self.purchases, "purchase_order_id"))
        self.assertTrue(hasattr(self.purchases, "employee_id"))
        