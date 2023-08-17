#!/usr/bin/env python3
"""
Exercise.py
"""
import redis
import uuid
from typing import Union


class Cache():
    """
    Cache class.
    """
    def __init__(self):
        """Initialize the class.
        set _redis to be the db and flush it/delete all keys
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data with a uuid generated and return uuid str
        """
        id_i = str(uuid.uuid4())
        datai = {id_i: data}
        self._redis.mset(datai)
        return id_i

    def get(self, key, fn=str):
        value = self._redis.get(key)
        if callable(fn):
            if value:
                return fn(value)
            return str(key)
        else:
            return value

    def get_str(self, key):
        """
        get a value and convert it to str
        """
        return self.get(key, str)

    def get_int(self, key):
        """
        get a value corresponding to the key and convert it to int.
        """
        return self.get(key, int)


if __name__ == "__main__":
    cache = Cache()
    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
        }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
