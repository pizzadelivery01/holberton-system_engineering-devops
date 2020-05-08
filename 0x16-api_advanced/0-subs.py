#!/usr/bin/python3
"""
request subs form reddit subreddit
"""


def number_of_subscribers(subreddit):
    """
    gets subs from provided subreddit
    """
    import requests

    subs = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "customized-agentV1.0"},
                        allow_redirects=False)
    if subs.status_code != 200:
        return 0
    else:
        return subs.json().get("data").get("subscribers")
