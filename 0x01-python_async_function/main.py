#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

# print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(2, 8)))
print(asyncio.run(wait_n(2, 0)))

# x = 5
# print(range(5))
# print(list(range(5)))