#!/usr/bin/python3

"""
This module contains routes for employees functionalities
in Benrays Store.
"""
from benrays_store.users.employees.employees_forms import EmployeeRegistration
from flask import Blueprint, render_template, redirect, url_for, flash

employee_bp = Blueprint("employee",
                        __name__,
                        template_folder="templates",
                        static_folder="static")


def init_form():
    """
    Initializes an instance of EmployeeRegistration class
    """
    form = EmployeeRegistration()
    return form

def save_data(form):
    """
    Sends a post request to Benrays Store Api with
    employee data from EmployeeRegistration form.
    """


# @employee_bp.route("/")
# def all_employees():
#     """
#     Sends a get request to Benrays Store Api and
#     returns all employees in the database
#     """
#     return render_template(
#         "employee.html",
#         title="Employees",
#         form=init_form(),
#     )


@employee_bp.route("/", methods=["GET", "POST"])
def employee():
    """
    Provides registration form for adding
    new employee.
    """
    form = init_form()
    if form.validate_on_submit():

        return render_template(
        "employee.html",
        title="Employees",
        form=form
    )
    
    flash("Employee was not registered due to invalid inputs. Please check!", "danger")
    return render_template(
        "employee.html",
        title="Employees",
        form=form
    )
