#!/usr/bin/python3
"""
Module for top ten hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code != 200:
        print('None')
    else:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
