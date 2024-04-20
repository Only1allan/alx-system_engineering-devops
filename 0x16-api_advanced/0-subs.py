#!/usr/bin/python3
"""
subscribers module
"""
import requests
from sys import argv


def number_of_subscribers(subbreddit):
    """Returns the number of subscribers for a given subreddit"""

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subbreddit), headers=header, timeout=5).json()

    try:
        return response.get("data").get("subscribers")
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
