#!/usr/bin/env python3 
"""A file that contains a wait"""
import asyncio


wR = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    result = []
    for i in range(n):
        wait_time = await wR(max_delay)
        result.append(wait_time)
    return sorted(result)
