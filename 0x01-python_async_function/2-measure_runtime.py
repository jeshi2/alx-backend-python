#!/usr/bin/env python3
"""
Module for measuring the total execution time for wait_n(n, max_delay).
"""

import time
from typing import List
from asyncio import run
from random import uniform
from asyncio import sleep

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time - Measures the total execution time for wait_n(n, max_delay).

    Returns:
        float: Total execution time divided by n.
    """
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
