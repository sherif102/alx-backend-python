#!/usr/bin/env python3
"""async comprehensions"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """generate an asyncrounous comprehension list"""
    return [yielded async for yielded in async_generator()]
