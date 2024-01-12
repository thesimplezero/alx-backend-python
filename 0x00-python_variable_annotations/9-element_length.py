#!/usr/bin/env python3
"""
Module with a function 'element_length' that returns a list of tuples.
Each tuple contains a sequence from the input iterable and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples. Each tuple contains a sequence and its length.

    Args:
        lst (Iterable[Sequence]): Input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples. Each tuple contains a
        sequence from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
