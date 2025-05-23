#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

# import asyncio
# import time

# it = time.time()
# asyncio.run(asyncio.sleep(2))
# lt = time.time()

# print(it)
# print(lt)
# print(lt - it)