#!/usr/bin/python3
"""
Module for list of hot titles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code != 200:
        return None
    else:
        for post in response.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
