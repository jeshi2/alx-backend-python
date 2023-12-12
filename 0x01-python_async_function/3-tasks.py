#!/usr/bin/env python3
"""
Module for creating an asyncio.Task using the wait_random coroutine.
"""

import asyncio
from typing import Any
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random - Creates an asyncio.Task using the wait_random coroutine.

    Returns:
        asyncio.Task: Task representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
