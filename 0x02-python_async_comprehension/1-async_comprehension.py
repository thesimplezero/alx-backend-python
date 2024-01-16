#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Collects 10 random floats asynchronously."""

import asyncio
from importlib import import_module
from typing import List

# Import using importlib for flexibility
async_generator = import_module("async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random floats with 1s intervals."""
    return [num async for num in async_generator()]


# Example usage:
async def main():
    numbers = await async_comprehension()
    print(numbers)

if __name__ == "__main__":
    asyncio.run(main())
