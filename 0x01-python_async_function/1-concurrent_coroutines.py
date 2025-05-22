#!/usr/bin/env python3
"""let's execute multiple coroutines at the same time with async"""


import asyncio
from typing import Callable


wait_random: Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """runs multiple coroutine functions simultaneously"""
    result: list = []
    for i in list(range(0, n)):
        result.append(await wait_random(max_delay))
    return result
