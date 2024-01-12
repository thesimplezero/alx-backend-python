#!/usr/bin/env python3

from typing import Tuple, List


def zoom_array(numbers: Tuple[int], factor: int = 2) -> List[int]:
    """
    Repeats each number in the input tuple based on the factor.

    Args:
        numbers (Tuple[int]): Input tuple of integers.
        factor (int, optional): Repeat factor. Defaults to 2.

    Returns:
        List[int]: List of integers after applying the zoom.
    """
    return [num for num in numbers for _ in range(factor)]


# Test the function
array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)
