#!/usr/bin/python3
"""
recursing module
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of all hot posts for a given subreddit"""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"}
    url = "https://www.reddit.com"
    query = "/r/{}/hot.json".format(subreddit)
    response = requests.get(url + query, headers=header,
                            params={"after": after}, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json()['data']['children']:
            hot_list.append(post['data']['title'])
        after = response.json()['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
