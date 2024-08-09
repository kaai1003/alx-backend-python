#!/usr/bin/env python3
"""duck typing annotations Module"""
from typing import Union, Sequence


def safe_first_element(lst: Sequence[any]) -> Union[any, None]:
    """safe first element"""
    if lst:
        return lst[0]
    else:
        return None
