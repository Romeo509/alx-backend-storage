#!/usr/bin/env python3
"""
web.py
"""

import requests
import redis
import time


redis_client = redis.Redis()


def get_page(url: str) -> str:
    """Fetches HTML content from a URL and caches
    the result with expiration."""

    redis_client.incr(f"count:{url}")

    cached_content = redis_client.get(f"content:{url}")
    if cached_content:
        return cached_content.decode('utf-8')

    response = requests.get(url)
    html_content = response.text

    redis_client.setex(f"content:{url}", 10, html_content)

    return html_content
