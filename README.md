# Asynchronous Web Crawler & Search Engine

## Overview
This project is an asynchronous web crawler and lightweight search engine built using Python.
It efficiently crawls web pages using non-blocking I/O, indexes their content, and enables fast
keyword-based search using a custom inverted index.

The goal of this project is to demonstrate backend fundamentals such as concurrency,
performance optimization, data structures, and scalable I/O-bound system design.

---

## Tech Stack
- Python 3
- asyncio
- aiohttp
- Non-blocking I/O

---

## System Architecture
- **Crawler**: Asynchronously fetches web pages using `aiohttp`
- **Parser**: Extracts and cleans text content from HTML pages
- **Indexer**: Builds and maintains an inverted index for fast keyword lookup
- **Search Engine**: Performs efficient keyword-based search on indexed data

---

## Key Features
- Asynchronous crawling using `asyncio` and `aiohttp`
- Controlled concurrency to maximize throughput without overwhelming resources
- Custom **inverted index** for efficient keyword search
- Sub-second keyword search across **5,000+ crawled web pages**
- Optimized memory and I/O utilization

---

## How It Works
1. URLs are scheduled and fetched asynchronously using non-blocking HTTP requests.
2. HTML content is parsed and cleaned.
3. Words are indexed into an inverted index structure.
4. Search queries retrieve matching documents efficiently from the index.

---

## How to Run Locally

### Prerequisites
- Python 3.9 or higher

### Steps
```bash
git clone https://github.com/<your-username>/async-web-crawler-search-engine.git
cd async-web-crawler-search-engine
pip install -r requirements.txt
python main.py
