#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response
"""
import requests
import sys


def fetch_url(url):
    """
    script that takes in a URL, sends a request to the URL and
    displays the body of the response
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        body = response.content
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")
    except requests.exceptions.HTTPError as e:
        print(f'Error code: {e.response.status_code}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fetch_url.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    fetch_url(url)
