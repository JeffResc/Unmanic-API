"""
Application Cache example.

Connect to Unmanic instance, update the application cache, then read data from it.
"""
import asyncio

from unmanic_api import Unmanic

async def main():
    async with Unmanic('localhost') as unmanic:
        await unmanic.update()

        print(unmanic.app.settings)
        print(unmanic.app.workers)
        print(unmanic.app.version)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
