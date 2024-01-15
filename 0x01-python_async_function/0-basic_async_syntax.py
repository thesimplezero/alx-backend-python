#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Asynchronous coroutine that takes in an integer argument

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine"""
    # Generate a random delay
    rand = random.uniform(0, max_delay)

    # Pause execution for the generated delay
    await asyncio.sleep(rand)

    # Return the generated random delay
    return rand
