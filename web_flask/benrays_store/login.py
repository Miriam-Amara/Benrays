#!/usr/bin/python3

"""
This module contains the route for users login
Benrays store
"""

from web_flask.config import api_employees_route
from benrays_store.login_form import LoginForm
from benrays_store.users.employees.auth_manager import Employee

from flask import Blueprint, render_template, url_for, redirect, flash
from flask import session
from flask_login import login_user
import requests

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Provides login functionaliies for users
    in Benrays store
    """
    form = LoginForm()
    if form.validate_on_submit():
        data = {"email": form.email.data, "password": form.password.data}
        url = api_employees_route("/data")
        response = requests.get(url, json=data)
        if response.status_code == 200:
            user_data = response.json()
            session["user"] = {
                "id": user_data["id"],
                "email": user_data["email"],
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
                "role": user_data["role"],
            }

            user = Employee(
                id=user_data["id"],
                email=user_data["email"],
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                role=user_data["role"],
            )
            login_user(user, form.remember_me.data)
            return redirect(url_for("employee.employee"))
        else:
            flash(
                "Login unsuccessful. Please check email and password.",
                "danger")
    return render_template(
        "login.html",
        form=form,
    )
