#!/usr/bin/python3
"""
print sorted count of words in titles of hot articles
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API and prints a sorted count of given keywords
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return
    else:
        for post in response.json().get('data').get('children'):
            title = post.get('data').get('title').lower().split()
            for word in word_list:
                if word.lower() in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        after = response.json().get('data').get('after')
        if after is None:
            if len(word_count) == 0:
                return
            for key, value in sorted(word_count.items(),
                                     key=lambda item: item[1], reverse=True):
                print(f'{key}: {value}')
            return
        return count_words(subreddit, word_list, word_count, after)
