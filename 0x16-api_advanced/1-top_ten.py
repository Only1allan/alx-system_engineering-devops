#!/usr/bin/python3
"""
top_ten module
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit"""

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = "https://www.reddit.com"
    query = "/r/{}/hot.json".format(subreddit)
    response = requests.get(url + query, headers=header, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
