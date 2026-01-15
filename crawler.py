import asyncio
import queue
import aiohttp
from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag

import json
from utils import clean_text

START_URLS = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Data_science"
]

MAX_PAGES = 5
CONCURRENCY = 3
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; AsyncCrawler/1.0)"
}
visited = set()
pages = {}

sem = asyncio.Semaphore(CONCURRENCY)

async def fetch(session, url):
    async with sem:
        try:
            async with session.get(
                url,
                headers=HEADERS,
                timeout=10,
                allow_redirects=True
            ) as resp:
                print("Fetching:", url, "Status:", resp.status)

                if resp.status == 200 and "text/html" in resp.headers.get("Content-Type", ""):
                    return await resp.text()
        except Exception as e:
            print("Fetch error:", e)
            return None

async def crawl(session, url):
    if url in visited or len(visited) >= MAX_PAGES:
        return
    print("Crawling:", url)
    visited.add(url)
    html = await fetch(session, url)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("div.mw-parser-output")

    if not content:
        return

    text = clean_text(content.get_text(" ", strip=True))

    pages[url] = text

    for link in soup.find_all("a", href=True):
        next_url = link["href"]
        if next_url.startswith("http"):
            await crawl(session, next_url)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [crawl(session, url) for url in START_URLS]
        await asyncio.gather(*tasks)
    print(f"Crawled {len(pages)} pages.")
    with open("data/pages.json", "w", encoding="utf-8") as f:
        json.dump(pages, f)

if __name__ == "__main__":
    asyncio.run(main())
