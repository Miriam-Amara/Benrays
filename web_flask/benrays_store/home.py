#!/usr/bin/python3

"""
This module provides functions for employees
registration, login, account update, deletion.
"""
import requests
from benrays_store.login_form import LoginForm
from flask import Blueprint, render_template, redirect, url_for, flash

home_bp = Blueprint("home", __name__, template_folder="templates")


@home_bp.route("/login", methods=['GET', 'POST'])
def login():
    """
    Allows employees to login to the store
    with their email and password
    """
    form = LoginForm()
    if form.validate_on_submit():
        from benrays_store import app, bcrypt
        url = "http://127.0.0.1:4000/api/v1/employees/data"
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        params = {"email": form.email.data, "password": form.password.data}
        headers = {"Accept": "application/json"}
        response = requests.get(url, json=params, headers=headers)
        if response.status_code == 200 and response.json()["role"] == "admin":
            return redirect(url_for("admin.admin"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)

