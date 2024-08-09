#!/usr/bin/env python3
"""element_length module"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length func"""
    return [(i, len(i)) for i in lst]
