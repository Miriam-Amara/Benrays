#!/usr/bin/python3

"""

"""

from views import app_views


@app_views.route("/status")
def status():
    """ Returns status code of requests """
    return {"status": "OK"}
