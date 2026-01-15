from indexer import build_index
import time

index = build_index()

while True:
    query = input("Search keyword (or 'exit'): ").strip()
    if query == "exit":
        break

    start = time.time()
    results = index.search(query)
    end = time.time()

    print(f"\nFound {len(results)} pages in {round((end-start)*1000, 2)} ms\n")
    for r in results[:10]:
        print(r)
