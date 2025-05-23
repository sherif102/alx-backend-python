#!/usr/bin/env python3
"""measure the runtime"""

import asyncio
import time
from typing import Callable, Awaitable, List

wait_n: Callable[
    [int, int],
    Awaitable[List[float]]] = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure total execution time for 'wait_n' function"""
    initial_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))

    return (time.time() - initial_time) / n
