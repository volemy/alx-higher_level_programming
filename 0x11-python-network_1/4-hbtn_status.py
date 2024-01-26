#!/usr/bin/python3
"""
Module with a python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def get_status():
    """
    script that fetches https://alx-intranet.hbtn.io/status
    """
    response = requests.get('https://alx-intranet.hbtn.io/status')
    body = response.content
    print("Body response:")
        print("     -type: {}".format(content_type))
        print("     -content: {}".format(body))
        print("     -utf8 content: {}".format(utf8_content))

if __name__ == "__main__":
    get_status()
