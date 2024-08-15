#!/usr/bin/env python3
"""A file that contains an asynchronous function"""
import asyncio
import random


def wait_random(max_delay: int = 10):
    """A function that waits for a random amount of time up to max_delay"""
    delay = asyncio.sleep(random.randint(0, max_delay))
    return delay
