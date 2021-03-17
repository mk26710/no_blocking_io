import asyncio
import functools
from typing import Callable

__all__ = ["to_thread"]


def to_thread(func: Callable):
    """Asynchronously run function `func` in a separate thread"""

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        partial = functools.partial(func, *args, **kwargs)
        coro = asyncio.to_thread(partial)
        return await coro

    return wrapper
