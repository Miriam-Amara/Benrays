#!/usr/bin/python3

"""
This module contains UpdateEmployee class for
updating the information of an employee in
Benrays Store database.
"""

from models import storage
from models.employees import Employee
from api.v1.views.employees import employees_bp
from api.v1.views.employees.utils import check_required_attributes
from api.v1.views.employees.utils import delete_attr

from flask_restful import Api, Resource, abort


api = Api(employees_bp)


class UpdateEmployee(Resource):
    """
    A class to update an employee information
    in the database.
    """

    def put(self, id):
        """
        Checks if employee exists in the database
        and updates the info.
        """
        data = check_required_attributes(passwd=False)
        if data["warehouses"]:
            del data["warehouses"]
        del data["password"]

        employee_exists = storage.get(Employee, id=id)
        if not employee_exists:
            abort(404, description="Employee not found")

        employee = list(employee_exists.values())[0]
        employee_data = employee.to_dict()

        for attr, value in data.items():
            if value != employee_data.get(attr):
                setattr(employee, attr, value)
        employee.save()

        delete_data = ["password", "permissions", "__class__"]
        delete_attr(employee_dict=employee_data, *delete_data)

        return employee_data, 200


api.add_resource(UpdateEmployee, "/update/<id>")
