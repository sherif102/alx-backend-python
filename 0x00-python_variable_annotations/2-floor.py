#!/usr/bin/env python3
"""basic annotations - floor"""


def floor(n: float) -> int:
    """returns the floor value of an integer"""
    ans = round(n) if round(n) < n else round(n) - 1
    return ans
