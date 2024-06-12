#!/usr/bin/env python3
"""Func spawns Tasks n times"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        n: num of times to spawn wait_random
        max_delay: maximum delay for each call
    """
    u = [task_wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(u)]
