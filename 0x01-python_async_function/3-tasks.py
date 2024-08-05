#!/usr/bin/env python3
"""async task Module"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """return async task"""
    return asyncio.create_task(wait_random(max_delay))
