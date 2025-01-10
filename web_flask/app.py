#!/usr/bin/python3
"""

"""
from benrays_store import app

for rule in app.url_map.iter_rules():
    print(rule)




if __name__ == "__main__":
    app.run(threaded=True, debug=True, host="0.0.0.0", port=5000)