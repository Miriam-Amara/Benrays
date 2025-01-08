#!/usr/bin/python3

"""
This module provides unit tests for Customer class
"""

from models.customers import Customer
import unittest


class TestCustomer(unittest.TestCase):
    """
    Defines test cases for the Customer class attributes and methods
    """
    def setUp(self):
        """ Instantiates the Customer class for each test methods """
        self.customer = Customer()
    
    def test_has_attributes(self):
        """
        Test that object of Customer class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.customer, "id"))
        self.assertTrue(hasattr(self.customer, "created_at"))
        self.assertTrue(hasattr(self.customer, "updated_at"))
        self.assertTrue(hasattr(self.customer, "first_name"))
        self.assertTrue(hasattr(self.customer, "last_name"))
        self.assertTrue(hasattr(self.customer, "phone_number"))
        self.assertTrue(hasattr(self.customer, "email"))
        self.assertTrue(hasattr(self.customer, "city"))
        self.assertTrue(hasattr(self.customer, "state"))
        self.assertTrue(hasattr(self.customer, "country"))
        self.assertTrue(hasattr(self.customer, "save"))
        self.assertTrue(hasattr(self.customer, "__str__"))

    def test_create_obj_with_kwargs(self):
        """ 
        Test that objects of Customer class can be created
        with keyword arguments
        """
        customer = Customer(first_name="Obinna",
                              city="LeftRight", state="Double"
                            )
        self.assertEqual(customer.first_name, "Obinna")
        self.assertEqual(customer.city, "LeftRight")
        self.assertEqual(customer.state, "Double")

    def test_save(self):
        """ Confirms objects are saved to database """
        customer = Customer(first_name="oooo", phone_number=84484, city="ooo",
                            state="ooo"
                        )
        customer.save()


if __name__ == "__main__":
    unittest.main()
