#!/usr/bin/env python3
"""async generator"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, float]:
    """asyncronously loop 10 times and yielding random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
