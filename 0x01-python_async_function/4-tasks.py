#!/usr/bin/env python3
"""
Module for creating asyncio.Tasks using the wait_random coroutine.
"""

import asyncio
from typing import List, Any
from asyncio import Task

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n - Asynchronously spawns task_wait_random n
    times with the specified max_delay.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks: List[Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = await asyncio.gather(*tasks)
    return delays
