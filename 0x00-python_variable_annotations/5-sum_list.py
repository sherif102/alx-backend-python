#!/usr/bin/env python3
"""complex types - list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """calculate the sum of all values in a list"""
    result: float = 0
    for value in input_list:
        result += value
    return result
