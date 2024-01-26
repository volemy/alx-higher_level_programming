#!/usr/bin/python3
"""
This module has a python script that takes a URL and an email
Sends a POST request to the passed URL with email as the parameter
 and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import sys
import urllib.parse


def post_email_request(url, email):
    """
    Script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter
    """
    data = urllib.parse.urlencode({"email": email})
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        content_type = response.getheader('content-type')
        if content_type and 'charset' in content_type:
            charset = content_type.split('charset=')[-1]
            body = body.decode(charset)
        print("Body response:")
        print("     -content:", body)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 send_post_email_request.py <URL> <EMAIL>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email_request(url, email)
