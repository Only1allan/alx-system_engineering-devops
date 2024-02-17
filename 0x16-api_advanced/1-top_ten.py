#!/usr/bin/python3
"""Module for top ten posts of a particular subreddit."""

import sys
import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the
      first 10 hot posts listed for a given subreddit."""
    user = {'User-Agent': 'Mozilla/5.0'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
