#!/usr/bin/env python3
"""
Cache module.
Provides a Cache class for storing and retrieving data in Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve the data from Redis and optionally
        convert it using a callable.

        Args:
            key (str): The key to retrieve.
            fn (Optional[Callable]): The function to convert the data.

        Returns:
            Union[str, bytes, int, float, None]:
            The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data from Redis and convert it to a string.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[str]: The retrieved data as
            a string, or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data from Redis and convert it to an integer.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[int]: The retrieved data as
            an integer, or None if the key does not exist.
        """
        return self.get(key, int)
