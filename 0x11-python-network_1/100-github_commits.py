#!/usr/bin/python3
"""
module that has a Python script that takes 2 arguments in order to
solve this challenge.
"""

import sys
import requests


def list_commits(repository, owner):
    """
    Python script that takes 2 arguments in order to
    solve this challenge.
    @arg_1 = repo name
    @arg_2 = owner name
    """
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 100-github_commits.py <repository> <owner>")
        sys.exit(1)
    repository = sys.argv[1]
    owner = sys.argv[2]
    list_commits(repository, owner)
