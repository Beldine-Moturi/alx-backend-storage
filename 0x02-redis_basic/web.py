#!/usr/bin/env python3
"""Defines the function get_page."""
import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """Decorator: counts the no. of times a function was called."""

    @wraps(method)
    def wrapper(url):
        """Wrapper function of the decorator."""
        r.incr("count:{}".format(url))
        count = r.get(f"cached:{url}")
        if count:
            return count.decode("utf-8")
        r.setex(f"cached:{url}", 10, method(url))
        return method(url)

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Obtains HTML content of a particular URL and returns it."""
    html = requests.get(url)
    return html.text
