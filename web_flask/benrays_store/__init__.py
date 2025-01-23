from benrays_store.users.employees.employees_routes import employee_bp

from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bycrpt = Bcrypt(app)

app.register_blueprint(employee_bp, url_prefix="/benrays_store/employees")

