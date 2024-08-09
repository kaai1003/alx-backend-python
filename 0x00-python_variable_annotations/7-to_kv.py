#!/usr/bin/env python3
"""to kv function Module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple with string & int or float"""
    return (k, float(v * v))
