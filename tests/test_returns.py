#!/usr/bin/python3

"""
This module provides unit tests for returns classes.
"""

import unittest
from models.returns import ReturnInward, ReturnOutward


class TestReturnInward(unittest.TestCase):
    """
    Defines test cases for the ReturnInward class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the ReturnInward class for each test method.
        """
        self.return_inwards = ReturnInward()

    def test_has_attributes(self):
        """
        Test that object of ReturnInward class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.return_inwards, "id"))
        self.assertTrue(hasattr(self.return_inwards, "created_at"))
        self.assertTrue(hasattr(self.return_inwards, "updated_at"))
        self.assertTrue(hasattr(self.return_inwards, "category_id"))
        self.assertTrue(hasattr(self.return_inwards, "product_id"))
        self.assertTrue(hasattr(self.return_inwards, "color_id"))
        self.assertTrue(hasattr(self.return_inwards, "quantity"))
        self.assertTrue(hasattr(self.return_inwards, "unit_selling_price"))
        self.assertTrue(hasattr(self.return_inwards, "total_price"))
        self.assertTrue(hasattr(self.return_inwards, "amount_paid"))
        self.assertTrue(hasattr(self.return_inwards, "payment_status"))
        self.assertTrue(hasattr(self.return_inwards, "payment_type"))
        self.assertTrue(hasattr(self.return_inwards, "warehouse_id"))
        self.assertTrue(hasattr(self.return_inwards, "customer_id"))
        self.assertTrue(hasattr(self.return_inwards, "reason"))
        self.assertTrue(hasattr(self.return_inwards, "employee_id"))




class TestReturnOutward(unittest.TestCase):
    """
    Defines test cases for the ReturnOutward class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the ReturnOutward class for each test method.
        """
        self.return_outwards = ReturnOutward()

    def test_has_attributes(self):
        """
        Test that object of ReturnOutward class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.return_outwards, "id"))
        self.assertTrue(hasattr(self.return_outwards, "created_at"))
        self.assertTrue(hasattr(self.return_outwards, "updated_at"))
        self.assertTrue(hasattr(self.return_outwards, "category_id"))
        self.assertTrue(hasattr(self.return_outwards, "product_id"))
        self.assertTrue(hasattr(self.return_outwards, "color_id"))
        self.assertTrue(hasattr(self.return_outwards, "quantity"))
        self.assertTrue(hasattr(self.return_outwards, "unit_cost_price"))
        self.assertTrue(hasattr(self.return_outwards, "total_price"))
        self.assertTrue(hasattr(self.return_outwards, "amount_paid"))
        self.assertTrue(hasattr(self.return_outwards, "warehouse_id"))
        self.assertTrue(hasattr(self.return_outwards, "supplier_id"))
        self.assertTrue(hasattr(self.return_outwards, "reason"))
        self.assertTrue(hasattr(self.return_outwards, "employee_id"))
