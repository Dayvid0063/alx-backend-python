#!/usr/bin/env python3
"""Method that safely gets value"""


from typing import Any, TypeVar, Mapping, Optional, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely gets and returns value from dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
