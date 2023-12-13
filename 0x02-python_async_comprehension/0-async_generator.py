#!/usr/bin/env python3
"""
Async Generator that yields random numbers.
"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that yields a random number between 0
      and 10 after waiting 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
