#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random
delay between 0 and max_delay (inclusive).
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random - Asynchronously waits for a random delay and returns it.

    Returns:
        float: Random delay between 0 and max_delay (inclusive).
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
