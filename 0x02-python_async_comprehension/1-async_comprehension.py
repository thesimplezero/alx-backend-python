#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Collect 10 floats async using comprehension."""

import asyncio
from .async_generator import async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """Gather 10 random floats async."""

    return [num async for num in async_generator()]
