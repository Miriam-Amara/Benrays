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
register_args.add_argument("salary", type=str,
                           help="salary"
                        )
register_args.add_argument("role", type=str,
                           required=True, help="employee role is required"
                        )
register_args.add_argument("authorization", type=str,
                           help="authorization"
                        )
register_args.add_argument("qualification", type=str,
                           help="qualification"
                        )



class Register(Resource):
    """
    Registers an employee on database
    """
    def post(self):
        """ creates a user in database """
        args = register_args.parse_args()
        email = args["email"]
        employee = storage.get(cls=Employee, email=email)
        if employee:
            abort(404, description="Employee already exists")
        employee = Employee(**args)
        employee.save()
        employee_data = employee.to_dict()
        del employee_data["password"]
        del employee_data["authorization"]
        del employee_data["__class__"]
        return employee_data, 201


api.add_resource(Register, "/register")