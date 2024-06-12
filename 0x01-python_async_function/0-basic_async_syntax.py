#!/usr/bin/env python3
"""Func waits a random delay and returns it"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random float between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
