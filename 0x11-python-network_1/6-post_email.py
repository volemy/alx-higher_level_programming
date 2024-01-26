#!/usr/bin/python3
"""
Script that takes URL and email address sends POST request to the passed URL
"""
import requests
import sys


def send_post_request(url, email):
    """
    Python script that takes in a URL and an email address,
    sends a POST request to the passed URL
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    body = response.content
    print("Body response:")
    print("     -type: <class 'bytes'>")
    print("     -content: {}".format(body))
    print("     -utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 send_post_request.py <URL> <EMAIL>")
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
