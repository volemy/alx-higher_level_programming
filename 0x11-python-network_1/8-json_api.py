#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
import requests
import sys

def search_user(letter):
    """
    script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user
    """
    if not letter:
        letter = ""

    data = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json['id'], response_json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) == 2 else ""
    search_user(letter)
