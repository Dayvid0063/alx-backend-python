#!/usr/bin/env python3
"""Func converts variable to a KV pair"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns coverted key and its value to a tuple"""
    return k, v ** 2
