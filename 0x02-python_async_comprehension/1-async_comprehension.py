#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Collects 10 random floats asynchronously using async comprehension."""

import asyncio
from .async_generator import async_generator  # Import for clarity
from typing import List


async def async_comprehension() -> List[float]:
    """
    Efficiently collects 10 random floats with 1-second
    intervals using async comprehension.

    Leverages the async_generator to yield random floats asynchronously.
    """

    return [num async for num in async_generator()]
