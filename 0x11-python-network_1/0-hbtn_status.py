#!/usr/bin/python3
"""
Module that outlines a python script that fetches
https://alx-intranet.hbtn.io/status
"""
import urllib.request


def fetch_status():
    """
    script to fetch https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        content_type = type(body)
        utf8_content = body.decode('utf-8')
        print("Body response:")
        print("     -type: {}".format(content_type))
        print("     -content: {}".format(body))
        print("     -utf8 content: {}".format(utf8_content))

if __name__ == "__main__":
    fetch_status()
