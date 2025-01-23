#!/usr/bin/python3

from dotenv import load_dotenv
import os

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
host = os.getenv("BENRAYS_STORE_HOST")
port = os.getenv("BENRAYS_STORE_PORT")

BASE_URL = "http://127.0.0.1:4000/"
BASE_PATH = "api/"
VERSION = "v1"
EMPLOYEES = "/employees"
headers = {"Content-Type": "application/json"}

def employees(PATH=""):
    return BASE_URL + BASE_PATH + VERSION + EMPLOYEES + PATH
