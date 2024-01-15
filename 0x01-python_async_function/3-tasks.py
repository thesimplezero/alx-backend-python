#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tasks"""

import asyncio

# Import the wait_random function from the specified module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task"""

    # Create and return an asyncio.Task for the wait_random coroutine
    return asyncio.create_task(wait_random(max_delay))
