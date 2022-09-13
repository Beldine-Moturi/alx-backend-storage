#!/usr/bin/env python3
"""Defines the function get_page."""
import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()

def count_calls(function: Callable) -> Callable:
    """Decorator: counts the no of times a function was called."""

    @wraps(function)
    def wrapper(url):
        """Wrapper function of the decorator."""
        r.incr("count:{}".format(url))
        count = r.get(f"cached:{url}")
        if count:
            return count.decode("utf-8")
        r.setex(f"cached:{url}", 10, function(url))
        return function

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Obtains HTML content of a particular URL and returns it."""
    html = requests.get(url)
    return html.text
