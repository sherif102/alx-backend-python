#!/usr/bin/env python3
"tasks 4"


import asyncio
from typing import Callable, List, Awaitable


task_wait_random: Callable[
    [int], asyncio.Task
    ] = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """runs multiple coroutine functions
    simultaneously and return thier runnin time"""
    result = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*result))
