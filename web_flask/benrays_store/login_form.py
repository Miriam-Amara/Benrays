#!/usr/bin/python3

"""
This module contains LoginForm class
for users login
"""


from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    A class that defines attributes and validators
    for users login system.
    """

    email = StringField(
        "Email",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your email"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter your password"},
    )
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")
