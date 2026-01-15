import json
from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def add_document(self, doc_id, text):
        for word in text.split():
            self.index[word].add(doc_id)

    def search(self, keyword):
        return list(self.index.get(keyword.lower(), []))

def build_index():
    with open("data/pages.json", encoding="utf-8") as f:
        pages = json.load(f)

    idx = InvertedIndex()
    for url, text in pages.items():
        idx.add_document(url, text)

    return idx
