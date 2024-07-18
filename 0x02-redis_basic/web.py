#!/usr/bin/env python3
"""web cache module """

import requests
import redis
from typing import Callable
from functools import wraps

redis_client = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """ Decorator wrapper """

    @wraps(fn)
    def wrapper(url):
        """ Wrapper for decorator """
        redis_client.incr(f"count:{url}")
        cached_res = redis_client.get(f"cached:{url}")
        if cached_res:
            return cached_res.decode('utf-8')
        result = fn(url)
        redis_client.setex(f"cached:{url}", 10, result)
        return result
    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """Get page self descriptive"""
    response = requests.get(url)
    return response.text
