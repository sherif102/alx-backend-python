#!/usr/bin/env python3
"""more involved type annotations"""


from typing import TypeVar, Any, Mapping, Union, Optional


# K = TypeVar('K')
# V = TypeVar('V')
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T | None = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
