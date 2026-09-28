from bookstore.pricing import price_with_tax


def test_price_with_tax():
    assert price_with_tax(100) == 118.0
