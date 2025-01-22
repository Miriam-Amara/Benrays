#!/usr/bin/python3

"""
This module contains AddCategory, AddProduct, and AddColor classes
for adding new products to Benrays Store Inventory.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired, Length


class AddCategory(FlaskForm):
    """
    This class provides attributes for adding
    new categories to Benrays Store Inventory
    Management system.
    """

    name = StringField(
        "Category Name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    submit = SubmitField("Save")


class AddColor(FlaskForm):
    """
    This class provides attributes for adding
    new colors to the system.
    """

    name = StringField("Color Name",
                       validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField("Save")


class AddProduct(FlaskForm):
    """
    This class provides attributes for adding new products to the system.
    """

    name = StringField(
        "Product Name", validators=[DataRequired(), Length(min=2, max=60)]
    )
    category_id = StringField("Category Id",
                              validators=[DataRequired(), Length(36)])
    colors_id = FieldList(
        StringField("Color IDs", validators=[DataRequired(), Length(36)]),
        min_entries=1
    )
    submit = SubmitField("Save")
