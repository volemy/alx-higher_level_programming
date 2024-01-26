#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
import urllib.request
import sys


def get_header(url):
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == "X-Request-Id":
                print("{}".format(header[1]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fetch_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_header(url)
