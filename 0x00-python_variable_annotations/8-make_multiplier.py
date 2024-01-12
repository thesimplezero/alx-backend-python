#!/usr/bin/env python3
"""
Module with 'make_multiplier' function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a number by 'multiplier'.

    Args:
        multiplier (float): Multiplier for the function.

    Returns:
        Callable[[float], float]: Function that multiplies
        input by 'multiplier'.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
