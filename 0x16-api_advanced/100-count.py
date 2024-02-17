#!/usr/bin/python3
"""Module for count_words function."""
import requests
import sys


def count_words(subreddit, word_list):
    """Function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, timeout=10)
    if response.status_code != 200:
        print()
    else:
        data = response.json().get('data').get('children')
        count = {}
        for word in word_list:
            count[word] = 0
        for post in data:
            title = post.get('data').get('title').lower().split()
            for word in word_list:
                count[word] += title.count(word.lower())
        for word, c in count.items():
            print('{}: {}'.format(word, c))
