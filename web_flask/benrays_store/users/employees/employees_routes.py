#!/usr/bin/python3

"""
This module contains routes for employees functionalities
in Benrays Store.
"""
from benrays_store.users.employees.employees_forms import EmployeeRegistration
from web_flask.config import employees, headers

from flask import Blueprint, render_template, redirect, url_for, flash
import requests


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

def post_data(form):
    """
    Submit employee data for validation and saving.

    Sends a POST request to the Benrays Store API with data 
    from the EmployeeRegistration form to validate and store 
    employee details in the database.
    """
    data = {}
    data["first_name"] = form.first_name.data
    data["middle_name"] = form.middle_name.data
    data["last_name"] = form.last_name.data
    data["age"] = form.age.data
    data["gender"] = form.gender.data
    data["marital_status"] = form.marital_status.data
    data["phone_number"] = form.phone_number.data
    data["email"] = form.email.data
    data["street"] = form.street.data
    data["city"] = form.city.data
    data["state"] = form.state.data
    data["password"] = form.password.data
    data["role"] = form.role.data
    data["work_experience"] = form.work_experience.data
    data["qualifications"] = form.qualifications.data
    data["name_of_guarantor"] = form.name_of_guarantor.data
    data["guarantor_contact"] = form.guarantor_contact.data
    data["salary"] = form.salary.data
    data["permissions"] = form.permissions.data
    data["warehouses"] = form.warehouses.data

    url = employees(PATH="/register")
    response = requests.post(url, json=data, headers=headers)

    return response


def get_employees():
    """
    Returns all employees stored in the database
    """
    url = employees("/")
    all_employees = requests.get(url)
    return all_employees



@employee_bp.route("/", methods=["GET", "POST"])
def employee():
    """
    Provides registration form for adding
    new employee.
    """
    from benrays_store import bycrpt

    form = init_form()
    all_employees = get_employees()

    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data).decode("utf-8")
        form.password.data = hashed_password
        response = post_data(form)
        if response.status_code == 201:
            return redirect(url_for("employee.employee"))
        elif response.status_code == 409:
            flash("Employee already exits")
    if form.errors:
        flash("Employee was not registered due to invalid inputs. Please check!", "danger")

    if all_employees.status_code == 200:
        employees  = all_employees.json()

    return render_template(
        "employee.html",
        title="Employees",
        form=form,
        employees=employees
    )

