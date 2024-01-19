#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import time


async def measure_runtime(async_func, num_runs=4):
    """Measures the total runtime of an asynchronous function."""

    start_time = time.time()
    await asyncio.gather(*(async_func() for _ in range(num_runs)))
    return time.time() - start_time


async def main():
    """Main function to execute the measurement."""

    async_generator = __import__('1-async_comprehension').async_comprehension
    total_runtime = await measure_runtime(async_generator)
    print(f"Total runtime: {total_runtime:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
