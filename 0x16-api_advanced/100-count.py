#!/usr/bin/python3
"""
Count keywords module
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Parses the title of all hot articles, and prints a sorted count of
    given keywords"""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"}
    url = "https://www.reddit.com"
    query = "/r/{}/hot.json".format(subreddit)
    response = requests.get(url + query, headers=header,
                            params={"after": after}, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json()['data']['children']:
            title = post['data']['title'].lower().split()
            for word in word_list:
                if word.lower() in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        after = response.json()['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, word_count, after)
        if len(word_count) == 0:
            return
        for key, value in sorted(word_count.items(),
                                 key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(key, value))
    else:
        return