#!/usr/bin/python3
"""

"""
from benrays_store import app
from config import secret_key, host, port

app.config["SECRET_KEY"] = secret_key

# for rule in app.url_map.iter_rules():
#     print(rule)
# print("Search paths for templates:", app.jinja_loader.searchpath)
# print(app.jinja_env.get_or_select_template("base.html"))
# print(app.jinja_env.get_or_select_template("employee.html"))


if __name__ == "__main__":
    if not host:
        host = "0.0.0.0"
    if not port:
        port = 5000
    app.run(threaded=True, debug=True, host=host, port=port)
