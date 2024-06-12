#!/usr/bin/env python3
"""Async routine that spawns wait_random n times"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        n: num of times to spawn wait_random
        max_delay: maximum delay for each call
    """
    u = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await t for t in asyncio.as_completed(u)]
