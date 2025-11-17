import asyncio
import time
from typing import Callable, Awaitable


class AsyncDataCache:
    def __init__(self, loader_func: Callable[[], Awaitable], ttl: int = 86400):
        self._data = None
        self._timestamp = 0
        self._ttl = ttl
        self._loader = loader_func
        self._lock = asyncio.Lock()

    async def get(self, force_refresh: bool = False):
        async with self._lock:
            if (
                    force_refresh
                    or self._data is None
                    or time.time() - self._timestamp > self._ttl
            ):
                self._data = await self._loader()
                self._timestamp = time.time()
        return self._data

    async def refresh(self):
        return await self.get(force_refresh=True)
