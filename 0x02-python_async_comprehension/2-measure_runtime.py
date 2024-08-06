#!/usr/bin/env python3
"""runtime measure Module"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runtime measure coroutine function"""
    start_t = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    runtime = time.time() - start_t
    return runtime
