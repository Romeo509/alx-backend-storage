#!/usr/bin/env python3
"""Module for fetching and caching
HTML content from URLs."""

import redis
import requests
from functools import wraps

data = redis.Redis()


def cached_content_fun(method):
    """Fetches HTML content of a url"""

    @wraps(method)
    def wrapper(url: str):
        cached_content = data.get(f"cached:{url}")
        if cached_content:
            return cached_content.decode('utf-8')

        content = method(url)
        data.setex(f"cached:{url}", 10, content)
        return content

    return wrapper


@cached_content_fun
def get_page(url: str) -> str:
    """tracks how many times a particular URL was accessed"""

    count = data.incr(f"count:{url}")
    content = requests.get(url).text

    return content
