#!/usr/bin/env python3
"""
Async routine wait_n that spawns wait_random n times
with the specified max_delay.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n - Asynchronously spawns wait_random n times with
    the specified max_delay.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = sorted([await wait_random(max_delay) for _ in range(n)])
    return delays
