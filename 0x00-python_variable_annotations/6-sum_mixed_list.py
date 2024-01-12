#!/usr/bin/env python3
"""
Module with 'sum_mixed_list' function to sum a list of ints and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of ints and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List of ints and floats.

    Returns:
        float: Sum of the list.
    """
    return sum(mxd_lst)
