"""
Basic information example.

Connect to Unmanic instance, get the version number and instance name.
"""
import asyncio

from unmanic_api import Unmanic

async def main():
    async with Unmanic('localhost') as unmanic:
        version = await unmanic.get_version()
        print(f"Version: {version}")

        name = await unmanic.get_installation_name()
        print(f"Name: {name}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
