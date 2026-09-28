"""Price calculations."""


def price_with_tax(amount: float, rate: float) -> float:
    """Tax rate is now passed explicitly so we can support multiple regions."""
    return round(amount * (1 + rate), 2)
