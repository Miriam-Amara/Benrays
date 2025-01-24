#!/usr/bin/python3

"""
This module contains Register class that
adds an employee to the database.
"""

from models import storage
from models.employees import Employee
from views.employees import employees_bp
from views.employees.utils import check_required_attributes
from views.employees.utils import delete_attr

from flask_restful import Api, Resource, abort


api = Api(employees_bp)


class Register(Resource):
    """
    A class to create a new employee instance and adds
    it to the database
    """
    def post(self):
      """ creates and add employee to the database """
      args = check_required_attributes()

      # check if the user exists in the database
      email = args["email"]
      employee = storage.get(cls=Employee, email=email)
      if employee:
         abort(409, description="Employee already exists")

      warehouses_id = args["warehouses"]
      del args["warehouses"]

      # adds employee to database
      employee = Employee(**args)
      employee.save()
      
      employee_data = employee.to_dict()
      delete_data = ["password", "permissions", "__class__"]
      delete_attr(employee_dict=employee_data, *delete_data)

      return employee_data, 201


api.add_resource(Register, "/register")
