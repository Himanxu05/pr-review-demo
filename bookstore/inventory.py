"""Book catalogue and stock management."""

BOOKS = {
    1: {"title": "Clean Code", "price": 450.0, "stock": 5},
    2: {"title": "Designing Data-Intensive Applications", "price": 899.0, "stock": 2},
    3: {"title": "The Pragmatic Programmer", "price": 520.0, "stock": 0},
}


def get_book(book_id: int) -> dict | None:
    """Return the book, or None if the id is unknown."""
    return BOOKS.get(book_id)


def in_stock(book_id: int, qty: int = 1) -> bool:
    book = get_book(book_id)
    return book is not None and book["stock"] >= qty
