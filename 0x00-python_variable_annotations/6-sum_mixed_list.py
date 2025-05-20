#!/usr/bin/env python3
"""complex types - mixed list"""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """calculate the sum of all values in a list"""
    result: float = 0
    for value in mxd_lst:
        result += value
    return result
