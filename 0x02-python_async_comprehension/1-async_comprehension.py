#!/usr/bin/env python3
"""A coroutine to return 10 random numbers"""


from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 random numbers using async comprehension"""
    return [num async for num in async_generator()]
