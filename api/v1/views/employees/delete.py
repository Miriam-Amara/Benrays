#!/usr/bin/python3

"""
This module contains DeleteEmployee class that
deletes an employee's information from
Benrays Store database.
"""

from models import storage
from models.employees import Employee
from views.employees import employees_bp

from flask_restful import Api, Resource, abort

api = Api(employees_bp)


class DeleteEmployee(Resource):
    """
    This class provides delete method for
    deleting an employee from the database
    """
    def delete(self, id):
        """
        Checks if the employee id exists in the
        database and deletes the employee information.
        """
        employee_exists = storage.get(Employee, id=id)
        if not employee_exists:
            abort(404, description="Employee not found")

        employee = list(employee_exists.values())[0]
        storage.delete(employee)
        storage.save()

        return 204

api.add_resource(DeleteEmployee, "/delete/<id>")
