from flask import Blueprint

employees_bp = Blueprint("employees", __name__)

from api.v1.views.employees.register import *
from api.v1.views.employees.get_employee import *

