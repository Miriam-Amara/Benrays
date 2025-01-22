#!/usr/bin/python3


"""
This module contains registration and login forms for
employees in Benrays Store.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField
from wtforms import TextAreaField, FieldList, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import EqualTo, NumberRange


class EmployeeRegistration(FlaskForm):
    """
    This class provides attributes specific to adding
    new employees in the system.
    """

    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=3, max=30)]
    )
    middle_name = StringField("Middle Name",
                              validators=[Length(min=3, max=30)])
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=3, max=30)]
    )
    age = IntegerField("Age",
                       validators=[DataRequired(),
                                   NumberRange(min=18, max=50)])
    gender = RadioField("Gender", validators=[DataRequired()],
                        choices=[("male", "Male"), ("female", "Female")])
    marital_status = RadioField(
                            "Marital Status",
                            validators=[DataRequired()],
                            choices=[("single", "Single"), ("married", "Married")]
                        )
    phone_number = StringField("Phone Number",
                               validators=[DataRequired(), Length(11)])
    email = StringField("Email",
                        validators=[DataRequired(), Email(), Length(max=60)])
    street = StringField("Street",
                         validators=[DataRequired(), Length(min=5, max=60)])
    city = StringField("City",
                       validators=[DataRequired(), Length(min=2, max=60)])
    state = StringField("State",
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=60)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[EqualTo("password")]
    )
    role = RadioField("Role",
                      validators=[DataRequired()],
                      choices=[("admin", "Admin"), ("salesperson", "Salesperson"),
                                ("secretary", "Secretary"), ("manager", "Manager")])
    work_experience = TextAreaField("Work Experience",
                                    validators=[Length(max=200)])
    qualifications = StringField("Qualifications",
                                 validators=[Length(min=5, max=150)])
    name_of_guarantor = StringField(
        "Name of Guarantor",
        validators=[DataRequired(), Length(min=5, max=150)]
    )
    guarantor_contact = StringField(
        "Guarantor's Phone Number", validators=[DataRequired(), Length(11)]
    )
    salary = FloatField("Salary", validators=[NumberRange(min=0.00)])
    permissions = StringField("Permissions", validators=[Length(max=200)])
    warehouses = FieldList(
        StringField("Warehouse Id", validators=[DataRequired(), Length(36)]),
        min_entries=1,
    )
    submit = SubmitField("Save")
