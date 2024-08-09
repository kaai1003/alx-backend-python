#!/usr/bin/env python3
"""list of mixed types module"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """returm sum of mixed list items"""
    sum: float = 0.0
    for item in mxd_lst:
        sum += item
    return sum
