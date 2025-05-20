#!/usr/bin/env python3
"""more involved type annotations"""


from typing import TypeVar, Any, Mapping, Union


# K = TypeVar('K')
# V = TypeVar('V')
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """return value from type annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
