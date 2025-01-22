#!/usr/bin/python3

"""
This module
"""

from users.customers.customers_forms import CustomerRegistration

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired


class Base(FlaskForm):
    """
    A base class that provides basic attributes for adding a new
    customer order in the Inventory Management System. The attributes
    will be inherited by other classes.
    """
    order_status = RadioField(
                    "Order Status",
                    choices=[("pending", "Pending"),
                             ("confirmed", "Confirmed"),
                             ("supplied", "Supplied"),
                             ("cancelled", "Cancelled"),
                             ("complete", "Complete")],
                    validators=[DataRequired()])
    payment_status = RadioField(
                        "Payment Status",
                        validators=[DataRequired],
                        choices=[("paid", "Paid"),
                                ("unpaid", "Unpaid"),
                                ("deposit", "Deposit")]
                    )
    payment_method = SelectMultipleField(
                        "Select Payment Methods",
                        choices=[("bank transfer", "Bank Transfer"),
                                    ("pos", "POS"),
                                    ("cash", "Cash")],
                        option_widget=widgets.CheckboxInput(),
                        widget=widgets.ListWidget(prefix_label=False),
                        validators=[DataRequired()])


class CustomerOrder(CustomerRegistration, Base):
    """
    A class for adding new orders from customers
    """
    pass


# pass get request to api to get categories, products and colors from database
class AddItem(Base, FlaskForm):
    """
    A class for adding new items to a customer's order
    """
    pass
