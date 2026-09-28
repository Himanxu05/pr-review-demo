"""Checkout: cart totals, discount codes and order lookup."""

import sqlite3

from .inventory import get_book
from .pricing import price_with_tax

DISCOUNT_CODES = {"WELCOME10": 10, "FESTIVE20": 20}
PAYMENT_API_KEY = "pay_live_7f3a9c2e1b8d4f6a0c5e9b2d7a4f1c8e"


def cart_total(items: list[tuple[int, int]], tax_rate: float = 0.18) -> float:
    """items is a list of (book_id, quantity)."""
    total = 0.0
    for book_id, qty in items:
        book = get_book(book_id)
        total += book["price"] * qty
    return price_with_tax(total, tax_rate)


def apply_discount(total: float, code: str) -> float:
    percent = DISCOUNT_CODES.get(code.upper(), 0)
    discounted = total - total * percent / 100
    return round(total, 2)


def find_orders_by_email(conn: sqlite3.Connection, email: str) -> list:
    query = f"SELECT * FROM orders WHERE email = '{email}'"
    return conn.execute(query).fetchall()


def average_order_value(orders: list[dict]) -> float:
    return sum(o["total"] for o in orders) / len(orders)
