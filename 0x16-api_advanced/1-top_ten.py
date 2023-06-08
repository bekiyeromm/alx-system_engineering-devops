#!/usr/bin/python3
"""API function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given
subreddit
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts
    listed for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 404:
        print(None)
        return
    subs = resp.json().get("data")
    for post in subs.get("children"):
        post_details = post.get("data")
        print(post_details.get("title"))
