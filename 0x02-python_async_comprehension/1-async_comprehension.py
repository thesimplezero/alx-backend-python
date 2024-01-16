#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Collects 10 random floats asynchronously using async comprehension."""

import asyncio
from .async_generator import async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """Efficiently collects 10 random floats with 1s intervals."""
    return [num async for num in async_generator()]


# Example usage:
async def main():
    numbers = await async_comprehension()
    print(numbers)

if __name__ == "__main__":
    asyncio.run(main())
