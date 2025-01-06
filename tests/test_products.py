#!/usr/bin/python3

"""
This module provides unit tests for Product class.
"""

import unittest
from models.products import Product, Category, Color, ProductColor


class TestProduct(unittest.TestCase):
    """
    Defines test cases for the Product class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Product class for each test method.
        """
        self.product = Product()

    def test_has_attributes(self):
        """
        Test that object of Product class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.product, "id"))
        self.assertTrue(hasattr(self.product, "created_at"))
        self.assertTrue(hasattr(self.product, "updated_at"))
        self.assertTrue(hasattr(self.product, "name"))
        self.assertTrue(hasattr(self.product, "category_id"))
        self.assertTrue(hasattr(self.product, "save"))
        self.assertTrue(hasattr(self.product, "__repr__"))



class TestCategory(unittest.TestCase):
    """
    Defines test cases for the Category class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Category class for each test method.
        """
        self.category = Category()

    def test_has_attributes(self):
        """
        Test that object of Category class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.category, "id"))
        self.assertTrue(hasattr(self.category, "created_at"))
        self.assertTrue(hasattr(self.category, "updated_at"))
        self.assertTrue(hasattr(self.category, "name"))
        self.assertTrue(hasattr(self.category, "save"))
        self.assertTrue(hasattr(self.category, "__repr__"))



class TestColor(unittest.TestCase):
    """
    Defines test cases for the Color class attributes and methods.
    """
    def setUp(self):
        """
        Instantiates the Color class for each test method.
        """
        self.color = Color()

    def test_has_attributes(self):
        """
        Test that object of Color class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.color, "id"))
        self.assertTrue(hasattr(self.color, "created_at"))
        self.assertTrue(hasattr(self.color, "updated_at"))
        self.assertTrue(hasattr(self.color, "name"))
        self.assertTrue(hasattr(self.color, "save"))
        self.assertTrue(hasattr(self.color, "__repr__"))








if __name__ == "__main__":
    unittest.main(verbosity=2)