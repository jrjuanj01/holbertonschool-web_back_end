#!/usr/bin/env python3
"""File that contains a measure time function"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import time


async def measure_time(n: int, max_delay: int) -> float:
    """Function that measures the time taken to execute wait_n n times"""

    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = start_time + end_time
    return total_time / n
