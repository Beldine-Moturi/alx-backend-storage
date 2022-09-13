#!/usr/bin/env python3
"""Redis basics"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts how many times Cache's methods are called"""

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper func of the decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache():
    """Redis class"""

    def __init__(self) -> None:
        """Instantiates the class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in the cache"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Gets data from the cache."""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Converts redis data to string."""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Converts redis data to int."""
        data = self._redis.get(key)
        return int(data)
