#!/usr/bin/env python3
"""
Module with 'safe_first_element' function.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Gets first element of a sequence or None if empty.

    Args:
        lst (Sequence[Any]): Input sequence.

    Returns:
        Union[Any, None]: First element or None.
    """
    if lst:
        return lst[0]
    else:
        return None
