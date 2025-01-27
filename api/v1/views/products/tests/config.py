#!/usr/bin/python3

BASE_URL = "http://127.0.0.1:4000"
URL_TYPE = "/api"
VERSION = "/v1"

headers = {"Content-Type": "application/json"}


def product_route(PATH=""):
    url = BASE_URL + URL_TYPE + VERSION + "/products" + PATH
    return url
