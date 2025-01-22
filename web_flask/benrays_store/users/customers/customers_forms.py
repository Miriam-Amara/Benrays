#!/usr/bin/python3


"""
This module contains registration forms for
customers of Benrays Store.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email


class CustomerRegistration(FlaskForm):
    """
    This class provides attributes specific to adding new
    customers in the system.
    """

    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=3, max=50)]
    )
    last_name = StringField("Last Name", validators=[Length(min=3, max=50)])
    gender = RadioField("Gender", validators=[DataRequired()],
                        choices=[("male", "Male"), ("female", "Female")])
    phone_number = StringField("Phone Number",
                               validators=[DataRequired(), Length(11)])
    email = StringField("Email", validators=[Email(), Length(max=60)])
    street = StringField("Street", validators=[Length(min=5, max=60)])
    city = StringField("City",
                       validators=[DataRequired(), Length(min=2, max=60)])
    state = StringField("State",
                        validators=[DataRequired(), Length(min=2, max=60)])
    country = StringField(
        "City", default="Nigeria",
        validators=[DataRequired(), Length(min=2, max=60)]
    )
    submit = SubmitField("Save")
