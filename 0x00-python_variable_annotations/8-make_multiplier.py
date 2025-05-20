#!/usr/bin/env python3
"""complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier function"""
    def to_multiply(value: float) -> float:
        return multiplier * value
    return to_multiply
