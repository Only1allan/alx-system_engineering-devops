#!/usr/bin/python3
"""Module for top ten posts of a particular subreddit."""

import sys
import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the
      first 10 hot posts listed for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, timeout=10)
    if response.status_code != 200:
        print('None')
        return
    data = response.json().get('data').get('children')
    for post in data:
        print(post.get('data').get('title'))
