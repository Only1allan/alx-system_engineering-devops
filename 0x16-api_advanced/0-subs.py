#!/usr/bin/python3
"""Module for number of subscribers in a particular subreddit."""

import sys
import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit."""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')

if __name__ == '__main__':
    number_of_subscribers(sys.argv[1])
