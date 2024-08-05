#!/usr/bin/env python3
"""multiple coroutines module"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    random_delays: List[float] = []
    list_delays: List[float] = []

    for _ in range(n):
        random_delays.append(
            wait_random(max_delay)
        )
    for done in asyncio.as_completed(random_delays):
        result = await done
        list_delays.append(result)
    return list_delays
