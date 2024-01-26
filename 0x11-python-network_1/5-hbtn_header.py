#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id
"""
import requests
import sys


def get_header(url):
    """
    cript that takes in a URL, sends a request to the URL and
    displays the value of the variable X-Request-Id
    """
    response = requests.get(url)
    headers = response.headers
    if 'X-Request-Id' in headers:
        print("{}".format(headers["X-Request-Id"]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_header.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    get_header(url)
