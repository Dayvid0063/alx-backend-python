#!/usr/bin/env python3
"""A coroutine that loop 10 times"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """yield a random number every second"""
    for u in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
