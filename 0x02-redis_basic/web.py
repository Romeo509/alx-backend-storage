#!/usr/bin/env python3
import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis connection
cache = redis.Redis()


def cache_request(func: Callable) -> Callable:
    """Decorator for caching HTTP requests and counting access."""
    @wraps(func)
    def wrapper(url: str) -> str:
        cache.incr(f'count:{url}')
        cached_response = cache.get(f'result:{url}')
        if cached_response:
            return cached_response.decode('utf-8')
        response = func(url)
        cache.setex(f'result:{url}', 10, response)
        return response
    return wrapper


@cache_request
def get_page(url: str) -> str:
    """Fetches HTML content of a URL."""
    return requests.get(url).text


# Example usage
if __name__ == "__main__":
    test_url = (
        "http://slowwly.robertomurray.co.uk/delay/5000/"
        "url/http://www.google.com"
    )
    print(get_page(test_url))  # Fetch and print the content of the URL
