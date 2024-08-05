#!/usr/bin/env python3
"""multiple coroutines module"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    random_delays: List[float] = []
    list_delays: List[float] = []

    for _ in range(n):
        random_delays.append(
            task_wait_random(max_delay)
        )
    for done in asyncio.as_completed(random_delays):
        result = await done
        list_delays.append(result)
    return list_delays
