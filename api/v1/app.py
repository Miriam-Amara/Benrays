#!/usr/bin/python3

"""
This module contains Flask app instance for
running the application.
A close_database function for closing the
database session.
"""

from models import storage
from api.v1.views import app

import os


@app.teardown_appcontext
def close_database(exception):
    """Closes database session"""
    storage.close()


# for rule in app.url_map.iter_rules():
#     print(rule)


if __name__ == "__main__":
    host = os.getenv("BENRAYS_API_HOST")
    port = os.getenv("BENRAYS_API_PORT")

    if not host:
        host = "0.0.0.0"
    if not port:
        port = 4000
    app.run(threaded=True, debug=True, host=host, port=port)
