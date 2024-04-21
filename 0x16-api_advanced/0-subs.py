#!/usr/bin/python3
"""
subscribers module
"""
import requests


def number_of_subscribers(subbreddit):
    """Returns the number of subscribers for a given subreddit"""

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = "https://www.reddit.com"
    query = "/r/{}/about.json".format(subbreddit)
    response = requests.get(url + query, headers=header, allow_redirects=False)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    return 0
