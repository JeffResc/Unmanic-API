"""
Pause resume example.

Connect to Unmanic instance, pause worker "W0", wait 5 seconds and resume worker "W0".
"""
import asyncio

from unmanic_api import Unmanic

async def main():
    async with Unmanic('localhost') as unmanic:
        print(await unmanic.pause_worker("W0"))
        await asyncio.sleep(5)
        print(await unmanic.resume_worker("W0"))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
