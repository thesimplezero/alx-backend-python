#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Alter wait_n function with asyncio.gather"""

import asyncio
from typing import List

# Import the wait_random function from the specified module
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Return the list of all the delays (float values)."""

    # Create a list of asyncio.Tasks for wait_random
    list_delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Use asyncio.gather to wait for all tasks to complete
    return await asyncio.gather(*list_delays)
