#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Measure the total execution time for wait_n(n, max_delay)"""

import time
import asyncio

# Import the wait_n function from the specified module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure total execution time"""

    # Record the start time
    start = time.time()

    # Run the wait_n function using asyncio.run
    asyncio.run(wait_n(n, max_delay))

    # Calculate the average execution time per coroutine
    end = (time.time() - start) / n

    # Return the average execution time per coroutine
    return end
