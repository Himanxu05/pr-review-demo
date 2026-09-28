"""Price calculations."""

GST_RATE = 0.18


def price_with_tax(amount: float, rate: float = GST_RATE) -> float:
    return round(amount * (1 + rate), 2)
