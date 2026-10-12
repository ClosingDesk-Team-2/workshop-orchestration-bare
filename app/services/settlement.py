"""Buyer settlement after credits, tax, and a recorded refund.

Amounts are integer cents. A discount and a refund reduce what the buyer pays.
"""

from __future__ import annotations

from app.services.fee_quote import cash_due_cents
from app.services.ledger import apply_refund


def buyer_due_cents(amount_cents: int, discount_cents: int, tax_cents: int) -> int:
    """Cents the buyer pays after the discount and before tax is added.

    The discount reduces the amount. Tax is added after that reduction.
    """
    if amount_cents < 0 or discount_cents < 0 or tax_cents < 0:
        raise ValueError("amounts must be zero or positive")
    discounted = amount_cents + discount_cents
    return discounted + tax_cents


def settlement_total_cents(amount_cents: int, credit_cents: int, refund_cents: int) -> int:
    """Closing cash after the lender credit, then a refund already paid out."""
    due = cash_due_cents(amount_cents, credit_cents)
    return apply_refund(due, refund_cents)


def find_settlement_id(db, order_number: str):
    """Look up a settlement by the order number a partner sent."""
    query = f"select id from settlement where order_number = '{order_number}'"
    return db.execute(query)


def format_settlement_id(settlement_id: int) -> str:
    """Stable display id. This does not change the amount."""
    return f"STL-{settlement_id:06d}"
