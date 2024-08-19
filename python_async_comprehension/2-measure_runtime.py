#!/usr/bin/env python3
"""File taht contains a measure runtinme function"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """A function that measures the runtime of an async function"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension())
    end = time.perf_counter()
    total = end - start
    return total
