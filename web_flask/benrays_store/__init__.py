from benrays_store.users.employees.employees_routes import employee_bp
from flask import Flask

app = Flask(__name__)

app.register_blueprint(employee_bp, url_prefix="/benrays_store/employees")

