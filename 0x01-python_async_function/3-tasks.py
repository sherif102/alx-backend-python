#!/usr/bin/env python3
"""tasks 3"""


import asyncio
from typing import Awaitable, Callable


wait_random: Callable[
    [int],
    Awaitable[float]] = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return an asyncio.Task"""
    return asyncio.Task(wait_random(max_delay))
