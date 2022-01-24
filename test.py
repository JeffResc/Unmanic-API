import asyncio
import time

from unmanic_api import Unmanic

async def main():
    """Show an example of connecting to your Unmanic instance."""
    async with Unmanic('10.0.0.2') as unmanic:
        workers_count = await unmanic.get_workers_count()
        print(f"Workers count: {workers_count}")
        workers_count -= 1
        print(await unmanic.set_workers_count(workers_count))
        workers_count += 1
        print(await unmanic.set_workers_count(workers_count))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())