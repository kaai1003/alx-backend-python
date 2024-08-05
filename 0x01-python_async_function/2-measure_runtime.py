#!/usr/bin/env python3
"""Measure runtime Module"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return runtime of wait_n coroutine"""
    start_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_t = time.time()
    aprox_runtime = (end_t - start_t) / n

    return aprox_runtime
