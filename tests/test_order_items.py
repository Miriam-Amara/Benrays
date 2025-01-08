#!/usr/bin/python3

"""
This module provides unit tests for order_items classes
"""

import unittest
from models.order_items import PurchaseOrder, CustomerOrder, TransferOrder


class TestPurchaseOrder(unittest.TestCase):
    """
    Provide test cases for PurchaseOrder class attributes and methods
    """
    def setUp(self):
        """
        Instantiates the PurchaseOrder class for each test method.
        """
        self.purchase_orders = PurchaseOrder()
    
    def test_has_attributes(self):
        """
        Test that object of PurchaseOrder class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.purchase_orders, "id"))
        self.assertTrue(hasattr(self.purchase_orders, "created_at"))
        self.assertTrue(hasattr(self.purchase_orders, "updated_at"))
        self.assertTrue(hasattr(self.purchase_orders, "category_id"))
        self.assertTrue(hasattr(self.purchase_orders, "product_id"))
        self.assertTrue(hasattr(self.purchase_orders, "color_id"))
        self.assertTrue(hasattr(self.purchase_orders, "quantity"))
        self.assertTrue(hasattr(self.purchase_orders, "unit_cost_price"))
        self.assertTrue(hasattr(self.purchase_orders, "total_price"))
        self.assertTrue(hasattr(self.purchase_orders, "order_id"))
        self.assertTrue(hasattr(self.purchase_orders, "supplier_id"))
        self.assertTrue(hasattr(self.purchase_orders, "employee_id"))
        self.assertTrue(hasattr(self.purchase_orders, "save"))
        self.assertTrue(hasattr(self.purchase_orders, "__str__"))


class TestCustomerOrder(unittest.TestCase):
    """
    Provide test cases for CustomerOrder class attributes and methods
    """
    def setUp(self):
        """
        Instantiates the CustomerOrder class for each test method.
        """
        self.customer_orders = CustomerOrder()
    
    def test_has_attributes(self):
        """
        Test that object of CustomerOrder class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.customer_orders, "id"))
        self.assertTrue(hasattr(self.customer_orders, "created_at"))
        self.assertTrue(hasattr(self.customer_orders, "updated_at"))
        self.assertTrue(hasattr(self.customer_orders, "category_id"))
        self.assertTrue(hasattr(self.customer_orders, "product_id"))
        self.assertTrue(hasattr(self.customer_orders, "color_id"))
        self.assertTrue(hasattr(self.customer_orders, "quantity"))
        self.assertTrue(hasattr(self.customer_orders, "unit_selling_price"))
        self.assertTrue(hasattr(self.customer_orders, "total_price"))
        self.assertTrue(hasattr(self.customer_orders, "order_id"))
        self.assertTrue(hasattr(self.customer_orders, "customer_id"))
        self.assertTrue(hasattr(self.customer_orders, "employee_id"))
        self.assertTrue(hasattr(self.customer_orders, "save"))
        self.assertTrue(hasattr(self.customer_orders, "__repr__"))


class TestTransferOrder(unittest.TestCase):
    """
    Provide test cases for TransferOrder class attributes and methods
    """
    def setUp(self):
        """
        Instantiates the TransferOrder class for each test method.
        """
        self.transfer_orders = TransferOrder()
    
    def test_has_attributes(self):
        """
        Test that object of TransferOrder class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.transfer_orders, "id"))
        self.assertTrue(hasattr(self.transfer_orders, "created_at"))
        self.assertTrue(hasattr(self.transfer_orders, "updated_at"))
        self.assertTrue(hasattr(self.transfer_orders, "category_id"))
        self.assertTrue(hasattr(self.transfer_orders, "product_id"))
        self.assertTrue(hasattr(self.transfer_orders, "color_id"))
        self.assertTrue(hasattr(self.transfer_orders, "quantity"))
        self.assertTrue(hasattr(self.transfer_orders, "unit_cost_price"))
        self.assertTrue(hasattr(self.transfer_orders, "total_price"))
        self.assertTrue(hasattr(self.transfer_orders, "order_id"))
        self.assertTrue(hasattr(self.transfer_orders, "transfer_type"))
        self.assertTrue(hasattr(self.transfer_orders, "warehouse_id"))
        self.assertTrue(hasattr(self.transfer_orders, "employee_id"))
        self.assertTrue(hasattr(self.transfer_orders, "save"))
        self.assertTrue(hasattr(self.transfer_orders, "__repr__"))
