#!/usr/bin/env python3
"""A file that contains a wait"""
from typing import List
wR = __import__('0-basic_async_syntax').wait_random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


async def wait_n(n: int, max_delay: int) -> List[float]:
    result = []
    for i in range(n):
        wait_time = await wR(max_delay)
        result.append(wait_time)
        result = bubble_sort(result)
    return result
