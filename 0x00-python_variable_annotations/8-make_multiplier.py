#!/usr/bin/env python3
"""Func takes a float multiplier as arg"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier func"""
    return lambda x: x * multiplier
