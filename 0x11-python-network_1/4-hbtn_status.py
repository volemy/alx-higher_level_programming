#!/usr/bin/python3
"""
Module with a python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def get_status():
    """
    script that fetches https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))

if __name__ == "__main__":
    get_status()
