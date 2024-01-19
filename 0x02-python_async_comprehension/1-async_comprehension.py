#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Collect 10 floats async using comprehension."""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Gather 10 random floats async."""
    return [i async for i in async_generator()]
