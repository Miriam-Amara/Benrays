from flask import Blueprint

products_bp = Blueprint("products", __name__)

from api.v1.views.products.create_products import *
from api.v1.views.products.read_products import *
from api.v1.views.products.update_products import *
from api.v1.views.products.delete_products import *
