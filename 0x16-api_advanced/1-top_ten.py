#!/usr/bin/python3
"""Module for top ten posts of a particular subreddit."""

import sys
import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the
      first 10 hot posts listed for a given subreddit."""
    results = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
        headers={'User-Agent': 'Mozilla/5.0'})
    if results.status_code == 200:
        response_data = results.json()
        titles = response_data['data']['children']
        for title in titles:
            print(title['data']['title'])
    else:
        print(None)
