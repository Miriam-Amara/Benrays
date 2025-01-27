#!/usr/bin/python3

"""
This module contains unittest for create_products
module.
"""
from models import storage
from models.products import Category, Product, Color
from api.v1.views.products.create_products import CreateCategory
from api.v1.views.products.tests.config import product_route

import unittest
import requests


class TestCreateCategory(unittest.TestCase):
    """
    A class that provides test cases for creating
    a new product category.
    """

    def test_201_status_code(self):
        """
        Test that a new category is added successfully
        to the database.
        """
        self.data = {"name": "Book"}
        category_dict = storage.get(Category, name=self.data.get("name"))
        if category_dict:
            category_obj = list(category_dict.values())[0]
            storage.delete(category_obj)
            storage.save()

        url = product_route("/category/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 201)

    def test_409_status_code(self):
        """ "
        Test category already exists in database
        """
        self.data = {"name": "Book"}
        url = product_route("/category/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 409)

    def test_400_status_code(self):
        """
        Test that None value for required data throws an error
        """

        self.data = {"name": None}
        url = product_route("/category/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 400)


class TestCreateProduct(unittest.TestCase):
    """
    A class that provides test cases for creating
    a new product.
    """

    def test_201_status_code(self):
        """
        Test that a new product is added successfully
        to the database.
        """
        # get product category id
        category_dict = storage.get(Category, name="Book")
        category_obj = list(category_dict.values())[0]
        category_id = category_obj.id

        self.data = {"name": "9/9 beed", "category_id": category_id}
        product_dict = storage.get(Product, name=self.data.get("name"))
        if product_dict:
            product_obj = list(product_dict.values())[0]
            storage.delete(product_obj)
            storage.save()

        url = product_route("/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 201)

    def test_409_status_code(self):
        """ "
        Test product already exists in database Error
        """
        # get product category id
        category_dict = storage.get(Category, name="Book")
        category_obj = list(category_dict.values())[0]
        category_id = category_obj.id

        self.data = {"name": "9/9 beed", "category_id": category_id}
        url = product_route("/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 409)

    def test_400_status_code(self):
        """
        Test that None value for required data throws an error
        """
        self.data = {"name": None, "category_id": None}
        url = product_route("/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 400)

        self.data = {"name": "interlock", "category_id": None}
        url = product_route("/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 400)

    def test_incomplete_args(self):
        """
        Test that error occurs if the required arguments
        are not provided completely.
        """
        self.data = {"name": "9/9 beed"}
        url = product_route("/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 400)


class TestCreateColor(unittest.TestCase):
    """
    A class that provides test cases for creating
    a new color.
    """

    def test_201_status_code(self):
        """
        Test that a new color is added successfully
        to the database.
        """
        self.data = {"name": "green"}
        color_dict = storage.get(Color, name=self.data.get("name"))
        if color_dict:
            color_obj = list(color_dict.values())[0]
            storage.delete(color_obj)
            storage.save()

        url = product_route("/color/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 201)

    def test_409_status_code(self):
        """ "
        Test color already exists in database Error
        """
        self.data = {"name": "green"}
        url = product_route("/color/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 409)

    def test_400_status_code(self):
        """
        Test that None value for required data throws an error
        """
        self.data = {"name": None}
        url = product_route("/color/register")
        response = requests.post(url, json=self.data)
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main(verbosity=2)
