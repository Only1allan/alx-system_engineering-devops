#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list of hot articles"""

import requests
import sys


def recurse(subreddit, hot_list=[]):
    """Function that queries the Reddit API and returns a list of hot articles"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, timeout=10)
    if response.status_code != 200:
        return None
    data = response.json().get('data').get('children')
    for post in data:
        hot_list.append(post.get('data').get('title'))
    return hot_list
