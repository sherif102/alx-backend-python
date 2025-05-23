#!/usr/bin/env python3
"""let's execute multiple coroutines at the same time with async"""


import asyncio
from typing import Callable, List, Awaitable


wait_random: Callable[
    [int],
    Awaitable[float]] = __import__(
        '0-basic_async_syntax'
        ).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """runs multiple coroutine functions simultaneously"""
    result = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*result)
