#!/usr/bin/python3


"""
This module contains registration form suppliers of Benrays Store.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class SupplierRegistration(FlaskForm):
    """
    This class provides attributes for adding new
    suppliers to the system.
    """

    company_name = StringField(
        "Company Name", validators=[DataRequired(), Length(min=2, max=100)]
    )
    phone_number = StringField("Phone Number",
                               validators=[DataRequired(), Length(11)])
    email = StringField("Email",
                        validators=[Email(), Length(max=100)])
    street = StringField("Street",
                         validators=[Length(min=5, max=60)])
    city = StringField("City",
                       validators=[DataRequired(), Length(min=2, max=60)])
    state = StringField("State",
                        validators=[DataRequired(), Length(min=2, max=60)])
    country = StringField(
        "City", default="Nigeria",
        validators=[DataRequired(), Length(min=2, max=60)]
    )
    submit = SubmitField("Save")
