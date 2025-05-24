#!/usr/bin/env python3
"""run time for four parallel comprehensions"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the runtime of async_comprehension"""
    to_run = [async_comprehension() for i in range(4)]
    initial_time = time.time()
    # await async_comprehension()
    await asyncio.gather(*to_run)
    return time.time() - initial_time
