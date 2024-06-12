#!/usr/bin/env python3
"""Func sums a list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the floats in the list"""
    if input_list is None:
        return 0
    else:
        return sum(input_list)
