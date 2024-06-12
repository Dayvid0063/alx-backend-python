#!/usr/bin/env python3
"""Func measures the total exec time for another function"""


import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Returns total time / n"""
    u = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    v = perf_counter()
    return (v - u) / n
