#!/usr/bin/python3

"""
This module provides unit tests for Orders class.
"""

import unittest
from models.orders import Order


class TestOrder(unittest.TestCase):
    """
    Defines test cases for the Orders class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Orders class for each test method.
        """
        self.orders = Order()

    def test_has_attributes(self):
        """
        Test that object of Order class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.orders, "id"))
        self.assertTrue(hasattr(self.orders, "created_at"))
        self.assertTrue(hasattr(self.orders, "updated_at"))
        self.assertTrue(hasattr(self.orders, "status"))
        self.assertTrue(hasattr(self.orders, "save"))
        self.assertTrue(hasattr(self.orders, "__str__"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
