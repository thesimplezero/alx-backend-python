#!/usr/bin/env python3
"""
Module with 'sum_list' function that sums a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats.

    Args:
        input_list (List[float]): Input list of floats.

    Returns:
        float: Sum of the list.
    """
    return sum(input_list)
