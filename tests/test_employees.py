#!/usr/bin/python3

"""
This module provides unit tests for Employee class
"""

from models.employees import Employee
import unittest


class Testemployee(unittest.TestCase):
    """
    Defines test cases for the Employee class attributes and methods
    """
    def setUp(self):
        """ Instantiates the Employee class for each test methods """
        self.employee = Employee()
    
    def test_has_attributes(self):
        """
        Test that object of employee class inherits from BaseModel
        and contains its own attributes
        """
        self.assertTrue(hasattr(self.employee, "id"))
        self.assertTrue(hasattr(self.employee, "created_at"))
        self.assertTrue(hasattr(self.employee, "updated_at"))
        self.assertTrue(hasattr(self.employee, "first_name"))
        self.assertTrue(hasattr(self.employee, "middle_name"))
        self.assertTrue(hasattr(self.employee, "last_name"))
        self.assertTrue(hasattr(self.employee, "phone_number"))
        self.assertTrue(hasattr(self.employee, "email"))
        self.assertTrue(hasattr(self.employee, "street"))
        self.assertTrue(hasattr(self.employee, "city"))
        self.assertTrue(hasattr(self.employee, "state"))
        self.assertTrue(hasattr(self.employee, "salary"))
        self.assertTrue(hasattr(self.employee, "role"))
        self.assertTrue(hasattr(self.employee, "authorization"))
        self.assertTrue(hasattr(self.employee, "qualification"))
        self.assertTrue(hasattr(self.employee, "save"))
        self.assertTrue(hasattr(self.employee, "__repr__"))

    def test_create_obj_with_kwargs(self):
        """ 
        Test that objects of employee class can be created
        with keyword arguments
        """
        employee = Employee(first_name="Chichi", middle_name="Ace", last_name="Hiller",
                            street="glory street", city="LeftRight", state="Double",
                            phone_number="08077777777", email="chichi@gmail.com",
                            role="Salesperson", salary=50000.00, authorization="read only",
                            qualification="secondary school"
                        )
        self.assertEqual(employee.first_name, "Chichi")
        self.assertEqual(employee.middle_name, "Ace")
        self.assertEqual(employee.street, "glory street")
        self.assertEqual(employee.city, "LeftRight")
        self.assertEqual(employee.state, "Double")

