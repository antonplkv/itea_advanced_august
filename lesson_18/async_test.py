import asyncio
import time
import random


async def freeze(id_):
    print(f'{id_} started')
    await asyncio.sleep(random.randint(0, 5))
    print(f'{id_} ended')


async def main():
    t1 = asyncio.create_task(freeze(1))
    t2 = asyncio.create_task(freeze(2))

    r1 = await t1
    r2 = await t2
    print(r1, r2)


asyncio.run(main())

