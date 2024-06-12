#!/usr/bin/env python3
"""Measure the execution time"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_com four times and return the total"""
    begin: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for u in range(4)))
    end: float = time.perf_counter()
    return (end - begin)
