#!/usr/bin/python3

"""

"""


from flask_login import UserMixin
from flask_login import LoginManager
from flask import session

login_manager = LoginManager()


class Employee(UserMixin):
    """
    A class that provides functionalites to handle
    user session.
    """

    def __init__(self, id, email, first_name, last_name, role):
        """Initializes current session user data"""
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role


@login_manager.user_loader
def load_user(user_id):
    """ """
    user_data = session.get("user")
    if user_data and user_data["id"] == user_id:
        return Employee(
            id=user_data["id"],
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
        )
    return None
