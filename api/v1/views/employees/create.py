#!/usr/bin/python3

"""

"""

from models import storage
from models.employees import Employee
from views.employees import employees_bp


from flask_restful import Api, Resource, reqparse, abort


api = Api(employees_bp)




register_args = reqparse.RequestParser()
register_args.add_argument("first_name", type=str,
                           required=True, help="first name is required"
                        )
register_args.add_argument("middle_name", type=str,
                           help="middle name"
                        )
register_args.add_argument("last_name", type=str,
                           required=True, help="last name is required"
                        )
register_args.add_argument("age", type=str,
                           required=True, help="age is required"
                        )
register_args.add_argument("gender", type=str,
                           required=True, help="gender is required"
                        )
register_args.add_argument("marital_status", type=str,
                           required=True, help="marital status is required"
                        )
register_args.add_argument("phone_number", type=str,
                           required=True, help="phone number is required"
                        )
register_args.add_argument("email", type=str,
                           required=True, help="email is required"
                        )
register_args.add_argument("password", type=str,
                           required=True, help="password is required"
                        )
register_args.add_argument("street", type=str,
                           required=True, help="street name is required"
                        )
register_args.add_argument("city", type=str,
                           required=True, help="city name is required"
                        )
register_args.add_argument("state", type=str,
                           required=True, help="state name is required"
                        )
register_args.add_argument("role", type=str,
                           required=True, help="employee role is required"
                        )
register_args.add_argument("salary", type=str)
register_args.add_argument("work_experience", type=str)
register_args.add_argument("qualification", type=str)
register_args.add_argument("name_of_guarantor", type=str,
                           required=True,
                           help="Name of guarantor role is required"
                        )
register_args.add_argument("guarantor_contact", type=str,
                           required=True,
                           help="Guarantor's phone number role is required"
                        )
register_args.add_argument("permissions", type=str,
                           help="permissions"
                        )
register_args.add_argument(
    "warehouses", type=str,
    required=True,
    help="Warehouses id where the employee manages is required")

def check_required_attributes():
   attr_list = ["first_name", "age", "gender",
           "marital_status", "phone_number", "email",
           "password", "street", "city", "state",
           "role", "name_of_guarantor", "guarantor_contact"]
   try:
      args = register_args.parse_args()
   except Exception:
      abort(400, description="post data must be json")
   
   for key, value in args.items():
      if key in attr_list and value is None:
         abort(400, description=f"{key} cannot be null")
   
   return args



class Register(Resource):
    """
    Registers an employee on database
    """
    def post(self):
      """ creates a user in database """
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
      del employee_data["password"]
      del employee_data["permissions"]
      del employee_data["__class__"]
      return employee_data, 201


api.add_resource(Register, "/register")
