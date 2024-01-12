#!/usr/bin/env python3
"""
Module with 'to_kv' function that returns a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a string and the square of a number.

    Args:
        k (str): Input string.
        v (Union[int, float]): Input number.

    Returns:
        Tuple[str, float]: Tuple of the string and the square of the number.
    """
    return k, float(v ** 2)
