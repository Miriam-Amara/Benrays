#!/usr/bin/python3

"""
This module provides:
Registration form,
Login form,
Update account form
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Provides registration functionalities
    """
    first_name = StringField("First Name",
                             validators=[DataRequired(), Length(min=2, max=60)])
    middle_name = StringField("Middle Name", validators=[Length(min=2, max=60)])
    last_name = StringField("Last Name",
                            validators=[DataRequired(), Length(min=2, max=60)])
    phone_number = StringField("Phone Number",
                               validators=[DataRequired(), Length(11)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=2, max=60)])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), Length(min=2, max=60), EqualTo("password")])
    street = StringField("Street Name",
                         validators=[DataRequired(), Length(min=2, max=60)])
    city = StringField("City", validators=[DataRequired(), Length(min=2, max=60)])
    state = StringField("State", validators=[DataRequired(), Length(min=2, max=60)])
    role = StringField("Role", validators=[DataRequired(), Length(min=2, max=20)])
    salary = FloatField("Salary")
    qualification = StringField("Qualification", validators=[Length(min=2, max=60)])
    authorization = StringField("Authorizataion", validators=[Length(min=2, max=20)])
    submit = SubmitField("Register")




# class LoginForm(FlaskForm):
#     """
#     provides login functionalities
#     """
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("Password",
#                              validators=[DataRequired(), Length(min=2, max=60)])
#     remember = BooleanField("Remember Me")
#     submit = SubmitField("Login")
