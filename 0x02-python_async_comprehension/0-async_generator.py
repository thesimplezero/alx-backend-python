#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Yields 10 random floats (0-10) with 1s intervals."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates 10 random floats."""

    for _ in range(10):
        try:
            await asyncio.sleep(1)
            yield random.uniform(0, 10)
        except Exception as e:
            print(f"Error during iteration: {e}")
