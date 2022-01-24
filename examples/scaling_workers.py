"""
Scaling workers example.

Connect to Unmanic instance and increase worker count by 1.
"""
import asyncio

from unmanic_api import Unmanic

async def main():
    async with Unmanic('localhost') as unmanic:
        workers_count = await unmanic.get_workers_count()
        print(f"Workers count: {workers_count}")

        workers_count += 1
        print(await unmanic.set_workers_count(workers_count))

        new_workers_count = await unmanic.get_workers_count()
        print(f"New workers count: {new_workers_count}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    