"""Server-url-handler implementation"""
import asyncio
import aiofiles
from typing import List
import aiohttp
from aiohttp import client_exceptions
from bs4 import BeautifulSoup


async def fetch_url(url: str):
    """Fetches one url"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                refs = []
                for link in soup.find_all('a'):
                    refs.append(link.get('href'))
                return url, refs

        except client_exceptions.ClientConnectorError:
            return url, "Ошибка подключения"


async def fetch_worker(que: asyncio.Queue, res_container: List):
    """executes tasks from queue"""
    while True:
        url = await que.get()

        result = await fetch_url(url)
        res_container.append(result)
        que.task_done()


async def fetch_all_urls(urls_path: str, request_count: int):
    """Fetches batch of urls"""
    que = asyncio.Queue()
    output = []
    workers = [asyncio.create_task(fetch_worker(que, output)) for _ in range(request_count)]

    async with aiofiles.open(urls_path, encoding="UTF-8") as urls:
        async for url in urls:
            await que.put(url)

    await que.join()

    for worker in workers:
        worker.cancel()

    return output
