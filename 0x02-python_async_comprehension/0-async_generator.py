#!/usr/bin/env python3
"""A coroutine that loop 10 times"""


import asyncio
import random


async def async_generator():
    """yield a random number every second"""
    for u in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
