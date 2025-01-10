#!/usr/bin/python3

"""

"""

from models import storage
from api.v1.views import app

from flask import Flask
import os


@app.teardown_appcontext
def close_database(exception):
    """ Closes database session """
    storage.close()

for rule in app.url_map.iter_rules():
    print(rule)



if __name__ == "__main__":
    host = os.getenv("BENRAYS_API_HOST")
    port = os.getenv("BENRAYS_API_PORT")

    if not host:
        host = "0.0.0.0"
    if not port:
        port = 5000
    app.run(threaded=True, debug=True, host=host, port=port)
