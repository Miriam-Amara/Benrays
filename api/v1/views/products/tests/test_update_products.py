#!/usr/bin/python3

"""
This module contains unittest for update_products
module.
"""
from models import storage
from models.products import Category, Product, Color
from api.v1.views.products.tests.config import product_route


import unittest
import requests


class TestUpdateCategory(unittest.TestCase):
    """
    A class that provides test cases for updating
    category in the database.
    """

    def test_200_status_code(self):
        """
        Test that a category is updated successfully in the database.
        """
        eye_dict = storage.get(Category, name="Eye")
        fish_dict = storage.get(Category, name="Fish")
        dict_list = [eye_dict, fish_dict]
        for dict_obj in dict_list:
            if dict_obj:
                obj = list(dict_obj.values())[0]
                storage.delete(obj)
                storage.save()

        category = Category(name="Eye")
        category.save()
        id = category.id

        url = product_route(f"/category/update/{id}")
        data = {"name": "Fish"}
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_400_status_code(self):
        """ "
        Test 400 status code is returned when:
            - No id is parsed.
            - Category name value is empty or None
            - The value to be updated already exists in database
        """
        category_dict = storage.get(Category, name="Break")
        if category_dict:
            category_obj = list(category_dict.values())[0]
            storage.delete(category_obj)
            storage.save()

        data = {"name": ""}
        category = Category(name="Break")
        category.save()
        id = category.id

        # test empty string
        url = product_route(f"/category/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

        # test for None value
        data = {"name": None}
        url = product_route(f"/category/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

        # test invalid id type
        data = {"name": 3455}
        url = product_route(f"/category/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

        # test category name already exists
        data = {"name": "Casement"}
        url = product_route(f"/category/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_404_status_code(self):
        """
        Test no id and category id not found
        """
        # test no id
        data = {"name": "Bell"}
        url = product_route("/category/update")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 404)

        # test empty id string
        url = product_route("/category/update/''")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 404)

        id = 458793
        data = {"name": "Bell"}
        url = product_route(f"/category/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 404)


class TestUpdateProduct(unittest.TestCase):
    """
    A class that provides test cases for updating
    a product in the database.
    """

    def test_200_status_code(self):
        """
        Test that a product is updated successfully in the database.
            - Deletes category if present in the database
            - Recreates the category
            - Sends a put request to Benrays store Api
            _ Confirms the category is updated
        """
        bird_dict = storage.get(Category, name="Bird")
        reptile_dict = storage.get(Category, name="Reptile")
        mammal_dict = storage.get(Category, name="Mammal")
        pigeon_dict = storage.get(Product, name="Pigeon")
        dict_list = [bird_dict, reptile_dict, mammal_dict, pigeon_dict]
        for obj_dict in dict_list:
            if obj_dict:
                obj = list(obj_dict.values())[0]
                storage.delete(obj)
                storage.save()

        category1 = Category(name="Bird")
        category2 = Category(name="Reptile")
        category3 = Category(name="Mammal")
        category1.save()
        category2.save()
        category3.save()
        product = Product(name="Pigeon", category_id=category1.id)
        product.save()

        id = product.id
        product_name = {"name": "Lizard"}
        url = product_route(f"/update/{id}")
        response = requests.put(url, json=product_name)
        self.assertEqual(response.status_code, 200)

        product_category = {"category_id": category2.id}
        url = product_route(f"/update/{id}")
        response = requests.put(url, json=product_category)
        self.assertEqual(response.status_code, 200)

        data = {"name": "Monkey", "category_id": category3.id}
        url = product_route(f"/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_400_status_code(self):
        """ "
        Test 400 status code is returned when:
            - No id is parsed.
            - Category name value is empty or None
        """
        # delete category and product from database if present
        vehicle_dict = storage.get(Category, name="Vehicle")
        break_dict = storage.get(Product, name="Break")
        dict_list = [vehicle_dict, break_dict]
        for obj_dict in dict_list:
            if obj_dict:
                obj = list(obj_dict.values())[0]
                storage.delete(obj)
                storage.save()

        # recreate category and product
        category = Category(name="Vehicle")
        category.save()
        product = Product(name="Break", category_id=category.id)
        product.save()
        id = product.id

        data = {"name": ""}
        url = product_route(f"/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

        data = {"name": None, "category_id": category.id}
        url = product_route(f"/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

        data = {"category_id": 3455}
        url = product_route(f"/category/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_404_status_code(self):
        """
        Test invalid product id and category id
        """
        data = {"name": ""}
        url = product_route("/update/")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 404)

        data = {"name": "hi"}
        url = product_route("/update/''")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 404)

        id = 458793
        data = {"name": "Bell", "category_id": "4567689"}
        url = product_route(f"/category/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 404)


class TestUpdateColor(unittest.TestCase):
    """
    A class that provides test cases for updating
    color in the database.
    """

    def setUp(self):
        """
        Deletes colors from database if presente
        """
        pink_dict = storage.get(Color, name="Pink")
        glaring_pink_dict = storage.get(Color, name="Glaring pink")
        dict_list = [pink_dict, glaring_pink_dict]
        for obj_dict in dict_list:
            if obj_dict:
                obj = list(obj_dict.values())[0]
                storage.delete(obj)
                storage.save()

    def test_200_status_code(self):
        """
        Test that color is updated successfully in the database.
        """

        name_exists = storage.get(Color, name="shiny-gold")
        if name_exists:
            color_obj = list(name_exists.values())[0]
            storage.delete(color_obj)
            storage.save()

        color = Color(name="Pink")
        color.save()

        id = color.id
        data = {"name": "shiny-gold"}
        url = product_route(f"/color/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_400_status_code(self):
        """ "
        Test 400 status code is returned when:
            - No id is parsed.
            - Color name value is empty or None
        """
        name_exists = storage.get(Color, name="Glaring pink")
        if name_exists:
            color_obj = list(name_exists.values())[0]
            storage.delete(color_obj)
            storage.save()

        color = Color(name="Glaring pink")
        color.save()
        id = color.id

        color_name_2 = {"name": ""}
        url = product_route(f"/color/update/{id}")
        response = requests.put(url, json=color_name_2)
        self.assertEqual(response.status_code, 400)

        color_name_3 = {"name": None}
        url = product_route(f"/color/update/{id}")
        response = requests.put(url, json=color_name_3)
        self.assertEqual(response.status_code, 400)

        data = {"name": 3455}
        url = product_route(f"/color/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_404_status_code(self):
        """
        Test invalid url and invalid id type
        """
        color_name_1 = {"name": "fishy_blue"}
        url = product_route("/color/update/''")
        response = requests.put(url, json=color_name_1)
        self.assertEqual(response.status_code, 404)

        color_name_1 = {"name": "fishy_blue"}
        url = product_route("/color/update/")
        response = requests.put(url, json=color_name_1)
        self.assertEqual(response.status_code, 404)

        id = 458793
        data = {"name": "reddish_radish"}
        url = product_route(f"/color/update/{id}")
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
