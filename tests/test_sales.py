#!/usr/bin/python3

"""
This module provides unit tests for Sale class.
"""

import unittest
from models.sales import Sale


class TestSale(unittest.TestCase):
    """
    Defines test cases for the Sale class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Sale class for each test method.
        """
        self.sales = Sale()

    def test_has_attributes(self):
        """
        Test that object of Sale class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.sales, "id"))
        self.assertTrue(hasattr(self.sales, "created_at"))
        self.assertTrue(hasattr(self.sales, "updated_at"))
        self.assertTrue(hasattr(self.sales, "category_id"))
        self.assertTrue(hasattr(self.sales, "product_id"))
        self.assertTrue(hasattr(self.sales, "color_id"))
        self.assertTrue(hasattr(self.sales, "quantity"))
        self.assertTrue(hasattr(self.sales, "unit_selling_price"))
        self.assertTrue(hasattr(self.sales, "total_price"))
        self.assertTrue(hasattr(self.sales, "amount_paid"))
        self.assertTrue(hasattr(self.sales, "customer_id"))
        self.assertTrue(hasattr(self.sales, "warehouse_id"))
        self.assertTrue(hasattr(self.sales, "payment_status"))
        self.assertTrue(hasattr(self.sales, "payment_type"))
        self.assertTrue(hasattr(self.sales, "customer_order_id"))
        self.assertTrue(hasattr(self.sales, "employee_id"))
        