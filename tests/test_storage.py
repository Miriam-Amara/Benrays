#!/usr/bin/python3

"""
This module provides unit test for DBStorage class
"""

import unittest
from models import storage
from models.products import Product, Category, Color
from models.warehouses import Warehouse


class TestStorage(unittest.TestCase):
    """
    Defines test cases for DBStorage class attributes and methods
    """
    def test_has_attr(self):
        """
        Confirms the required methods are
        present in the DBStorage class.
        """
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))
        self.assertTrue(hasattr(storage, "delete"))
        self.assertTrue(hasattr(storage, "close"))

    def test_all(self):
        """ Comfirms objects are returned from the database """
        category = Category(name="hgfc")
        product1 = Product(name="77ff", category_id=category.id)
        product2 = Product(name="wkhe", category_id=category.id)
        product3 = Product(name="dppp", category_id=category.id)
        color1 = Color(name="pink")
        color2 = Color(name="sky blue")
        category.save()
        product1.save()
        product2.save()
        product3.save()
        color1.save()
        color2.save()
        product1.colors.append(color1)
        product1.colors.append(color2)
        from models import storage
        storage.save()
        print("\n\nFrom all method")
        print(storage.all())
        print("\n\n")
        print(storage.all(Product))
    
    def test_get(self):
        warehouse = Warehouse(name="WH4", phone_number="898474", street="kiejj",
                              city="dees", state="ckiieii"
                            )
        warehouse.save()
        obj = storage.get(Warehouse, name=warehouse.name)
        print("\n\nFrom get method")
        print(warehouse.name)
        print(obj)
        print("\n\n")

    def test_count(self):
        """
        Confirms that total number of all objects of a given class is returned
        when the class name is passed as an argument. Or
        The total number of objects of all classes in the database is returned.
        """
        warehouse_count = storage.count(Warehouse)
        product_count = storage.count(Product)
        category_count = storage.count(Category)
        colors_count = storage.count(Color)
        all_classes_count = storage.count()
        print("\n\nFrom count method")
        print("total warehouses: ", warehouse_count)
        print("total products: ", product_count)
        print("total categories: ", category_count)
        print("total colors: ", colors_count)
        print("total objects: ", all_classes_count)
        print("\n\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
