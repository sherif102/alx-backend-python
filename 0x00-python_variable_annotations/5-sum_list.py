#!/usr/bin/env python3
"""complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    result: float = 0
    for value in input_list:
        result += value
    return result
