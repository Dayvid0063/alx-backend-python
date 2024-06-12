#!/usr/bin/env python3
"""Func measures the total exec time for another function"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total time / n"""
    begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - begin) / n
