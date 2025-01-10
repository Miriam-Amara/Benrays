BASE_URL = "http://127.0.0.1:5000/"
BASE_PATH = "api/"
VERSION = "v1"

EMPLOYEES = "/employees"

def get_employees():
    return BASE_URL + BASE_PATH + VERSION + EMPLOYEES
