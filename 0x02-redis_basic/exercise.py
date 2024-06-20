#!/usr/bin/env python3
"""
Cache module.
Provides a Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize the Cache class.
        Create a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
