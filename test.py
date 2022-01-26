"""
Basic information example.

Connect to Unmanic instance, get the version number and instance name.
"""
import asyncio

from unmanic_api import Unmanic

async def main():
    async with Unmanic('unmanic.jeffresc.dev', 443, tls=True) as unmanic:
        ver = await unmanic.get_version()
        print(ver)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
