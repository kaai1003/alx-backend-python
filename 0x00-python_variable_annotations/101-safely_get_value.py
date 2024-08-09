#!/usr/bin/env python3
"""duck typing annotations Module"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safely get value func"""
    if key in dct:
        return dct[key]
    else:
        return default
