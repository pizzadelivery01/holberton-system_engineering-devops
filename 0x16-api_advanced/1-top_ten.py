#!/usr/bin/python3
"""
gets top ten hot posts
"""


def top_ten(subreddit):
    """
    get top ten hot posts for subreddit
    """
    import requests

    subs = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "customizedv1.0"},
                        allow_redirects=False)
    if subs.status_code != 200:
        print("None")
    else:
        [print(child.get("data").get("title"))
         for child in subs.json().get("data").get("children")]
