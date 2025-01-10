#!/usr/bin/python3

"""
This module provides LoginForm class
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class LoginForm(FlaskForm):
    """
    provides login functionalities
    """
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=2, max=60)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
