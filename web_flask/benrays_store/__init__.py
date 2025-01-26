from benrays_store.users.employees.employees_routes import employee_bp
from benrays_store.users.employees.auth_manager import login_manager
from benrays_store.login import login_bp

from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bycrpt = Bcrypt(app)
login_manager.init_app(app)

app.register_blueprint(employee_bp, url_prefix="/benrays_store/employees")
app.register_blueprint(login_bp, url_prefix="/benrays_store/users")
