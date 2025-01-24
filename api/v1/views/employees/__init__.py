from flask import Blueprint

employees_bp = Blueprint("employees", __name__)

from views.employees.create import *
from api.v1.views.employees.get_employee import *
from api.v1.views.employees.update import *
from api.v1.views.employees.delete import *
