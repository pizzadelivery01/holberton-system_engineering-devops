#!/usr/bin/python3
"""
gets all hot articles
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    gets all hot articles
    """
    import requests

    subs = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        params={"count": count, "after": after},
                        headers={"User-Agent": "customizedv1.0"},
                        allow_redirects=False)
    if subs.status_code >= 400:
        return None

    new_hot = hot_list + [child.get("data").get("title")
                          for child in subs.json().get("data")
                          .get("children")]

    data = subs.json()
    if not data.get("data").get("after"):
        return new_hot
    return recurse(subreddit, new_hot, data.get("data").get("count"),
                   data.get("data").get("after"))
