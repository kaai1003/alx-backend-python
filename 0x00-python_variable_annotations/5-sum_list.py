#!/usr/bin/env python3
"""sum list func Module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of list items"""
    sum: float = 0.0
    for f in input_list:
        sum += f
    return sum
