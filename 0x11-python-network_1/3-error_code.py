#!/usr/bin/python3
"""
Module with script that takes in a URL and sends request to the URL
"""
import urllib.request
import sys
import urllib.error


def get_url(url):
    """
    Script that takes in a URL and sends a request to the URL
    """
    try:
        with  urllib.request.urlopen(url) as response:
            body = response.read()
            content_type = response.getheader('Content_Type')
            if content_type and 'charset' in content_type:
                charset = content_type.split('charset=')[1]
                body = body.decode(charset)
            print('Body response:')
            print('     -content:', body)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_url.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    get_url(url)
