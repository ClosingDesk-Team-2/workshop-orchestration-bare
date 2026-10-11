from app.services.fee_quote import format_money


def test_format_money_keeps_cents():
    assert format_money(1234) == "12.34"


def test_format_money_zero():
    assert format_money(0) == "0.00"
