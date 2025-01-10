from benrays_store.home import home_bp
from benrays_store.employees.admin import admin_bp
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SECRET_KEY"] = "5df6a4eebd5628cc9bf9b2d16e0ad415"
bcrypt = Bcrypt(app)

app.register_blueprint(home_bp, url_prefix="/store")
app.register_blueprint(admin_bp, url_prefix="/store/admin")


