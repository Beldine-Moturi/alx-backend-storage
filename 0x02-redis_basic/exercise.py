#!/usr/bin/env python3
"""Redis basics"""
import redis
import uuid
from typing import Union


class Cache():
    """Redis class"""

    def __init__(self) -> None:
        """Instantiates the class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """Generates a random key"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
