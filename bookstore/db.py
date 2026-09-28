"""SQLite helpers."""

import sqlite3


def connect(path: str = "bookstore.db") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def orders_for_user(conn: sqlite3.Connection, user_id: int) -> list:
    return conn.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,)).fetchall()
