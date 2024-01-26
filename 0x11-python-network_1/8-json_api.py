#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
import requests
import sys
import json

def search_user(x):
    """
    Python script that takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
    """
    if x is None:
        x = ""
    data = {'x': x}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    response_body = response.content.decode('utf-8')
    try:
        response_json = json.loads(response_body)
        if response_json:
            print("[{}] {}".format(response_json['id'], response_json['name']))
        else:
            print("No result")
    except json.JSONDecodeError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python3 8-json_api.py [letter]")
        sys.exit(1)
    elif len(sys.argv) == 2:
        search_user(sys.argv[1])
    else:
        search_user(None)
