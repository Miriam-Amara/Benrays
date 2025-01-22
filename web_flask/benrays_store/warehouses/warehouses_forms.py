#!/usr/bin/python3

"""
This module contains AddWarehouse class for
adding a new warehouse to Benrays Store
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class AddWarehouse(FlaskForm):
    """
    A class for adding new warehouses to Benrays Store.
    """
    name = StringField("Warehouse Name", validators=[DataRequired(), Length(min=3, max=60)])
    phone_number = StringField("Phone Number", validators=[DataRequired(), Length(11)])
    street = StringField("Street",
                         validators=[DataRequired(), Length(min=5, max=60)])
    city = StringField("City",
                       validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField("State",
                        validators=[DataRequired(), Length(min=2, max=20)])
