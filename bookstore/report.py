"""Daily sales report."""

from .pricing import price_with_tax


def daily_revenue(sales: list[float]) -> float:
    return sum(price_with_tax(s) for s in sales)
