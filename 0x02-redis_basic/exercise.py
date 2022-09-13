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


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a method in
    Cache's class method
    """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper of decorator."""
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, method(self, *args))
        return method(self, *args, **kwargs)

    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls of a particular function."""
    key = method.__qualname__
    r_instance = method.__self__._redis
    times_called = r_instance.get(key).decode("utf-8")
    inputs = r_instance.lrange(key + ":inputs", 0, -1)
    outputs = r_instance.lrange(key + ":outputs", 0, -1)
    zipped = zip(inputs, outputs)

    print(f"{key} was called {times_called} times:")
    for input, output in zipped:
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print(f"{key}(*{input}) -> {output}")


class Cache():
    """Redis class"""

    def __init__(self) -> None:
        """Instantiates the class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
