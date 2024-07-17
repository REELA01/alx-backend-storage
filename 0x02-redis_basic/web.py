#!/usr/bin/env python3
"""cache and tracker mod"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ decorator """
    @wraps(method)
    def wrapper(url):
        cached_ky = "cached:" + url
        cached_data = store.get(cached_ky)
        if cached_data:
            return cached_data.decode("utf-8")
        count_ky = "count:" + url
        html = method(url)
        store.incr(count_ky)
        store.set(cached_ky, html)
        store.expire(cached_ky, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """return HTML content of a url"""
    res = requests.get(url)
    return res.text
