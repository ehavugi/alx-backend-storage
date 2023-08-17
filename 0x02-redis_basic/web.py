#!/usr/bin/env python3
"""
Track url fetches
"""
import requests
import redis
from datetime import timedelta
import time
storage_ = redis.Redis()


def get_page(url: str) -> str:
    """
    Get url data and retun it
    Store the count get_page got called.
    """
    data = requests.get(url)
    keyUrl = "count:{}".format(url)
    print(keyUrl)
    counts = storage_.get(keyUrl)
    if counts:
        counts = int(counts)
    else:
        counts = 0

    storage_.mset({keyUrl: counts + 1})
    storage_.expire(keyUrl, timedelta(seconds=10))
    return data


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(storage_.get("count:{}".format(url)))
    get_page(url)
    get_page(url)
    print(storage_.get("count:{}".format(url)))
    get_page(url)
    print(get_page)
    print(storage_.get("count:{}".format(url)))
