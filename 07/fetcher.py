"""Main function"""
import argparse
import asyncio
import aiofiles
from url_handler import fetch_all_urls


parser = argparse.ArgumentParser('url_fetcher')
parser.add_argument("-c", dest="query_count", type=int, default=10, action="store")
parser.add_argument("url_path", type=str, action="store")
args = parser.parse_args()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
res = asyncio.run(fetch_all_urls(args.url_path, args.query_count))
print(res)
