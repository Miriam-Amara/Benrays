#!/usr/bin/python3

"""
This module provides Login class for
Employees login
"""

from  views.employees import employees_bp
from models import storage
from  models.employees import Employee

from flask_restful import Api, Resource, reqparse, abort

api = Api(employees_bp)




get_employee_args = reqparse.RequestParser()
get_employee_args.add_argument("email", type=str,
                           required=True, help="email is required"
                        )
get_employee_args.add_argument("password", type=str,
                           required=True, help="password is required"
                        )


class EmployeeByEmail(Resource):
    """
    Retrieves an employee from the database based on email
    and password
    """
    def get(self):
        """
        Checks if an employee exists in the database and retrieves
        the employee's data.
        """
        from views import bcrypt
        args = get_employee_args.parse_args()
        email = args["email"]
        password = args["password"]

        # get user from database
        employee = storage.get(cls=Employee, email=email)
        if not employee:
            abort(400, description="User not found")

        employee_data = list(employee.values())[0]
        hashed_password = employee_data.password
        print("\nchecking password hash:", bcrypt.check_password_hash(hashed_password, password))
        if not bcrypt.check_password_hash(hashed_password, password):
            abort(404, description="Password does not match")
        # print(db_password)
        # if not bcrypt.check_password_hash(db_password, password):

        employee_data = employee_data.to_dict()
        del employee_data["password"]
        del employee_data["authorization"]
        del employee_data["__class__"]
        return employee_data, 200
        

    

class EmployeeByID(Resource):
    """
    Provides a method to retrieve an employee from database
    by employees's id
    """
    def get(self, id):
        """ Retrieves an employee from database using the id """
        employee = storage.get(Employee, id=id)

        if not employee:
            abort(404, description="Not found")

        employee_data = list(employee.values())[0].to_dict()
        del employee_data["password"]
        del employee_data["authorization"]
        del employee_data["__class__"]
        return employee_data
        


class GetEmployees(Resource):
    """
    Get all employees in the database
    """
    def get(self):
        """ 
        Retrieves all objects of Employee class
        from database.
        """
        employees = []
        all_employees = storage.all(cls=Employee)

        for employee in all_employees.values():
            employee_data = employee.to_dict()
            del employee_data["password"]
            del employee_data["authorization"]
            del employee_data["__class__"]
            employees.append(employee_data)
        return employees, 200
    

class EmployeeCount(Resource):
    """
    Provides get method that retrieves the
    total number of employees in the database
    """
    def get(self):
        """
        Retrieves the total number of employees in the database
        """
        total_count = storage.count(cls=Employee)
        if not total_count:
            abort(404, description="Zero")
        return {"total_no_employees": total_count}, 200



api.add_resource(GetEmployees, "/")
api.add_resource(EmployeeCount, "/count")
api.add_resource(EmployeeByID, "/<string:id>")
api.add_resource(EmployeeByEmail, "/data")