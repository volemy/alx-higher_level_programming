#!/usr/bin/pyth0n3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


def github_id(username, password):
    """
    Function to fetch the user ID using GitHub API.
    """
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("id")
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 10-my_github.py <username> <password>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    github_id = get_github_id(username, password)
    print(github_id)
