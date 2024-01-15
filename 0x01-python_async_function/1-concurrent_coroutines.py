#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Import previous wait_random function and write an async routine"""

import asyncio
from typing import List

# Import the wait_random function from the specified module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of awaited responses"""

    # Use asyncio.gather to concurrently wait for n wait_random calls
    res = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    # Sort the results and return the list
    return sorted(res)
