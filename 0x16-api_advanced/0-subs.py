#!/usr/bin/env python
"""Reddit API"""
import requests
def number_of_subscribers(subreddit):
    """
    Query Reddit’s public API for total subscribers of a given subreddit.
    Returns the subscriber count (int), or 0 if the subreddit is invalid or any error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python:number_of_subscribers:v1.0 (by /u/yourusername)'}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if res.status_code != 200:
            return 0
        return res.json().get('data', {}).get('subscribers', 0)
    except (requests.RequestException, ValueError):
        return 0
