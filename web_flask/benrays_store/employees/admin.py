#!/usr/bin/python3

"""
This module provides functions for benrays store admin
"""
import requests
from benrays_store.employees.forms import RegistrationForm
from flask import Blueprint, render_template, redirect, url_for, flash

admin_bp = Blueprint("admin", __name__,
                     static_folder="static",
                     static_url_path="/static", 
                     template_folder="templates")

@admin_bp.route("/", methods=['GET', 'POST'])
def admin():
    """
    Provides admin functionalities
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        from benrays_store import app, bcrypt
        url = "http://127.0.0.1:4000/api/v1/employees/register"
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        data = {    "first_name": form.first_name.data,
                    "middle_name": form.middle_name.data,
                    "last_name": form.last_name.data,
                    "phone_number": form.phone_number.data,
                    "email": form.email.data,
                    "password": form.password.data,
                    "street": form.street.data,
                    "city": form.city.data,
                    "state": form.state.data,
                    "role": form.role.data,
                    "salary": form.salary.data,
                    "qualification": form.qualification.data,
                    "authorization": form.authorization.data,
                }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        print(response.json())
        if response.status_code == 201:
            flash(f"Account created for {form.first_name.data} {form.last_name.data}", "success")


    return render_template("admin.html", title="Admin", form=form)

