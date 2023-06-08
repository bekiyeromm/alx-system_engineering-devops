#!/usr/bin/python3
"""API a function that queries the Reddit API and returns
the number of subscribers (total subscribers) for a given
subreddit. If an invalid
subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subsribers for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 404:
        subs = response.json().get("data").get("subscribers")
        return subs
    return 0
