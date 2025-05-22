#!/usr/bin/env python3
"""the basics of async"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asyncronously waith for a delay time"""
    digit = random.random() * 100 / max_delay
    await asyncio.sleep(digit)
    return digit
