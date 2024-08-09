#!/usr/bin/env python3
"""make_multiplier Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier func"""
    return lambda n: n * multiplier
