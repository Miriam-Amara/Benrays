#!/usr/bin/python3

"""
This module contains routes for employees functionalities
in Benrays Store.
"""
from web_flask.config import api_employees_route, headers
from benrays_store.users.employees.employees_forms import EmployeeRegistration

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user, current_user
from flask import request
import requests


employee_bp = Blueprint(
    "employee", __name__, template_folder="templates", static_folder="static"
)


def init_form():
    """
    Initializes an instance of EmployeeRegistration class
    """
    form = EmployeeRegistration()
    return form


def get_employees():
    """
    Returns all employees stored in the database
    """
    url = api_employees_route("/")
    all_employees = requests.get(url)
    return all_employees


def get_employee_by_id(id):
    """
    Returns an employee information from api
    """
    url = api_employees_route(f"/{id}")
    employee = requests.get(url)
    return employee


@employee_bp.route("/", methods=["GET", "POST"])
@login_required
def employee():
    """
    Provides registration form for adding
    new employee.
    """
    from benrays_store import bycrpt

    first_name = current_user.first_name
    last_name = current_user.last_name
    role = current_user.role

    form = init_form()
    all_employees = get_employees()
    employees = ""

    if form.validate_on_submit():
        hashed_password = (bycrpt
                           .generate_password_hash(form.password.data)
                           .decode("utf-8"))
        form.password.data = hashed_password
        url = api_employees_route(PATH="/register")
        response = requests.post(url, json=form.data, headers=headers)
        if response.status_code == 201:
            return redirect(url_for("employee.employee"))
        elif response.status_code == 409:
            flash(
                f"{form.first_name.data} {form.last_name.data} "
                "already exits in database"
            )
    if form.errors:
        flash(
            "Employee was not registered due to invalid inputs. Please check!",
            "danger"
        )

    if all_employees.status_code == 200:
        employees = all_employees.json()

    return render_template(
        "employee.html",
        title="Employees",
        form=form,
        employees=employees,
        post_data=True,
        first_name=first_name,
        last_name=last_name,
        role=role,
    )


@employee_bp.route("/update/<id>", methods=["GET", "POST"])
@login_required
def update(id):
    """
    Sends PUT request to api and updates employee's info
    """

    first_name = current_user.first_name
    last_name = current_user.last_name
    role = current_user.role

    form = init_form()
    all_employees = get_employees()
    employee_exists = get_employee_by_id(id)
    employee_data = employee_exists.json()
    form.password.validators = []

    if request.method == "GET":
        form.first_name.data = employee_data.get("first_name")
        form.middle_name.data = employee_data.get("middle_name")
        form.last_name.data = employee_data.get("last_name")
        form.age.data = employee_data.get("age")
        form.gender.data = employee_data.get("gender")
        form.marital_status.data = employee_data.get("marital_status")
        form.phone_number.data = employee_data.get("phone_number")
        form.email.data = employee_data.get("email")
        form.street.data = employee_data.get("street")
        form.city.data = employee_data.get("city")
        form.state.data = employee_data.get("state")
        form.salary.data = employee_data.get("salary")
        form.work_experience.data = employee_data.get("work_experience")
        form.qualifications.data = employee_data.get("qualifications")
        form.name_of_guarantor.data = employee_data.get("name_of_guarantor")
        form.guarantor_contact.data = employee_data.get("guarantor_contact")
        form.role.data = employee_data.get("role")

    if form.validate_on_submit():
        url = api_employees_route(f"/update/{id}")
        requests.put(url, json=form.data, headers=headers)
        return redirect(url_for("employee.employee"))

    if form.errors:
        flash("Update was not successful. Please check your inputs!", "danger")

    if all_employees.status_code == 200:
        all_employees_data = all_employees.json()

    return render_template(
        "employee.html",
        form=form,
        employees=all_employees_data,
        offcanvas=True,
        first_name=first_name,
        last_name=last_name,
        role=role,
    )


@employee_bp.route("/delete/<id>", methods=["POST"])
@login_required
def delete(id):
    """
    Deletes an Employee information from the database
    """
    url = api_employees_route(f"/delete/{id}")
    requests.delete(url)
    return redirect(url_for("employee.employee"))


@employee_bp.route("/logout")
def logout():
    """
    Logs an employee out from the session
    """
    logout_user()
    return redirect(url_for("login.login"))
