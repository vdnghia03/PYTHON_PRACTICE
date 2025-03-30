# **An introduction to asyncIO**

AsyncIO is a Python library for asynchronous I/O. It is built around the coroutines of Python and provides tools to manage them and handle the I/O in an efficient way.

AsyncIO allows tasks to be performed concurrently rather than sequentially. This can be useful in scenarios where a task has to wait for something - for example, a response from a server or a read from a file. By allowing other tasks to be executed during this waiting time, the overall execution time of the program can be significantly reduced.

### **Key Components of asyncIO:**

1. **Coroutines**: Coroutines are functions that can be paused and resumed. This makes them ideal for I/O operations because they can be paused while waiting for input or output, allowing other tasks to run in the meantime.
2. **Tasks**: Tasks are a type of coroutine that are managed by the AsyncIO event loop. When a task is created, it is scheduled to run on the event loop.
3. **Event Loop**: The event loop is the core of every AsyncIO application. It schedules and executes tasks and callbacks, handles I/O, and manages system events.

# **Example of using AsyncIO in Python**

Here is a basic example of how AsyncIO can be used. Imagine we have a process that retrieves the contents of a web page and calculates the length of the returned file. We might simply write this using Python **`requests`** as follows:

```python
import requests
import time

def fetch(url):
    return requests.get(url).text

def run_requests():
    urls = [
        'https://dagster.io',
        'http://python.org',
        'https://docs.python.org/3/library/asyncio.html',
        'https://github.com/python/asyncio',
    ]

    start_time = time.time()

    for url in urls:
        result = fetch(url)
        print(len(result))

    end_time = time.time()
    print(f'All requests completed in {(end_time - start_time):.2f} seconds')

if __name__ == "__main__":
    run_requests()
```

Which would take a few seconds, then return the results:

```bash
80938
50572
19715
189497
All requests completed in 3.27 seconds

```

Let's now run the same task with the implementation of AsyncIO and the **`aiohttp`** library (which uses asyncio internally) and measure how long it takes for them all to finish.

```python
import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as response:
        result = await response.text()
        print(f'Fetched {url}, Length: {len(result)} characters')
        return result

async def main():
    urls = [
        'https://dagster.io',
        'http://python.org',
        'https://docs.python.org/3/library/asyncio.html',
        'https://github.com/python/asyncio',
    ]

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f'All requests completed in {(end_time - start_time):.2f} seconds')

# Python 3.7+
asyncio.run(main())
```

By fetching the pages concurrently, we significantly improve the performance of our process. Also note that the order in which the pages were retrieved is different than in the sequential approach.

```bash
Fetched https://dagster.io, Length: 80938 characters
Fetched https://docs.python.org/3/library/asyncio.html, Length: 19704 characters
Fetched http://python.org, Length: 50310 characters
Fetched https://github.com/python/asyncio, Length: 189502 characters
```
All requests completed in 1.03 seconds
