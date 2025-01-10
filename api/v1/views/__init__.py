from views.employees import employees_bp

from flask import Flask
from flask_bcrypt import Bcrypt

app =Flask(__name__)
bcrypt = Bcrypt(app)

app.register_blueprint(employees_bp, url_prefix="/api/v1/employees")

