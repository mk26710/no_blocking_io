# no-blocking-io

Minimal package that wraps `asyncio.to_thread` into a decorator.

## Example

```python
import asyncio
import time

from no_blocking_io import to_thread


@to_thread
def foo():
    time.sleep(5)
    print("foo")


async def bar():
    await asyncio.sleep(6)
    print("bar")


async def main():
    await asyncio.gather(foo(), bar())


asyncio.run(main())
```