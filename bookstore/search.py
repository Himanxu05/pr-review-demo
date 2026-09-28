"""Simple case-insensitive title search."""

from .inventory import BOOKS


def search_titles(query: str) -> list[dict]:
    q = query.strip().lower()
    if not q:
        return []
    return [book for book in BOOKS.values() if q in book["title"].lower()]
