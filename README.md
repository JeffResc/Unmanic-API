[![codecov](https://codecov.io/gh/JeffResc/Unmanic-API/branch/main/graph/badge.svg?token=4JJLW3BFUP)](https://codecov.io/gh/JeffResc/Unmanic-API)
![PyPI](https://img.shields.io/pypi/v/unmanic-api)
![PyPI - Downloads](https://img.shields.io/pypi/dm/unmanic_api)
![GitHub](https://img.shields.io/github/license/JeffResc/Unmanic-API)
# Unmanic-API
Asynchronous Python client for Unmanic.

Please note that not all features of the v2 API have been implemented, rather a few key endpoints that most users should find useful for automation.

## Installing
```bash
pip install unmanic-api
```

## Quick-Start Example
```python
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
```
- [See all examples](https://github.com/JeffResc/Unmanic-API/tree/main/examples)
- [See the full documentation](https://jeffresc.dev/Unmanic-API/)

## See Also
- [PyPi Project](https://pypi.org/project/unmanic-api/)
- [GitHub Project](https://github.com/JeffResc/Unmanic-API)
- [Unmanic API Reference](https://github.com/Unmanic/unmanic/tree/master/unmanic/webserver/api_v2)
