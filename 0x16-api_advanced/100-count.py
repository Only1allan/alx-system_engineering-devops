#!/usr/bin/python3
"""Module for count_words function."""
import requests
import sys


def count_words(subreddit, word_list, found={}, after=None):
    """Function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords."""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, timeout=10)
    if response.status_code != 200:
        return None
    data = response.json().get('data').get('children')
    for post in data:
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                if word in found:
                    found[word] += 1
                else:
                    found[word] = 1
    after = response.json().get('data').get('after')
    if after is None:
        if not found:
            return
        for key, value in sorted(found.items(), key=lambda item: item[1],
                                 reverse=True):
            print('{}: {}'.format(key, value))
    else:
        return count_words(subreddit, word_list, found, after)
