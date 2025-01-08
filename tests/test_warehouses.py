#!/usr/bin/python3

"""
This module provides unit tests for Warehouse class
"""

from models.warehouses import Warehouse
from models.employees import Employee
from models.products import Product, Category

import unittest


class TestWarehouse(unittest.TestCase):
    """
    Defines test cases for the Warehouse class attributes and methods
    """
    def setUp(self):
        """ Instantiates the Warehouse class for each test methods """
        self.warehouse = Warehouse()
    
    def test_has_attributes(self):
        """
        Test that object of Warehouse class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.warehouse, "id"))
        self.assertTrue(hasattr(self.warehouse, "created_at"))
        self.assertTrue(hasattr(self.warehouse, "updated_at"))
        self.assertTrue(hasattr(self.warehouse, "name"))
        self.assertTrue(hasattr(self.warehouse, "phone_number"))
        self.assertTrue(hasattr(self.warehouse, "street"))
        self.assertTrue(hasattr(self.warehouse, "city"))
        self.assertTrue(hasattr(self.warehouse, "state"))
        self.assertTrue(hasattr(self.warehouse, "save"))
        self.assertTrue(hasattr(self.warehouse, "__str__"))

    def test_create_obj_with_kwargs(self):
        """ 
        Test that objects of Warehouse class can be created
        with keyword arguments
        """
        warehouse = Warehouse(name="WH1", street="glory street",
                              city="LeftRight", state="Double"
                            )
        self.assertEqual(warehouse.name, "WH1")
        self.assertEqual(warehouse.street, "glory street")
        self.assertEqual(warehouse.city, "LeftRight")
        self.assertEqual(warehouse.state, "Double")


    def test_save(self):
        """ Confirms objects are saved to database """
        warehouse1 = Warehouse(name="WH1", phone_number="0958574",
                               street="aaa", city="aaaa", state="aaaa"
                            )
        warehouse2 = Warehouse(name="WH2", phone_number="067849",
                               street="bbb", city="bbb", state="bbbb"
                            )

        employee1 = Employee(first_name="ccc", last_name="ccc", phone_number="98777",
                             password="hdiel", street="ccc", city="ccc", state="ccc",
                             role="ccc"
                        )
        employee2 = Employee(first_name="ddd", last_name="ddd", phone_number="8988",
                             street="ddd", city="ddd", state="ddd", role="ddd",
                             password="kdiekee",
                        )
        category = Category(name="hghghg")
        product1 = Product(name="qqq", category_id=category.id)
        product2 = Product(name="zzz", category_id=category.id)
        product3 = Product(name="ggg", category_id=category.id)

        warehouse1.save()
        warehouse2.save()
        employee1.save()
        employee2.save()
        category.save()
        product1.save()
        product2.save()
        product3.save()

        from models import storage
        warehouse1.employees.append(employee1)
        warehouse1.employees.append(employee2)
        warehouse1.products.append(product1)
        warehouse1.products.append(product2)
        warehouse2.products.append(product3)
        warehouse2.products.append(product1)
        storage.save()


if __name__ == "__main__":
    unittest.main(verbosity=2)
