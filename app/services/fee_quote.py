"""Cash due at closing.

The lender credit reduces what the buyer pays. A quote that adds the credit
charges the buyer more than the closing statement.
"""

from __future__ import annotations


def cash_due_cents(amount_cents: int, credit_cents: int) -> int:
    """Return the cents the buyer still owes after the lender credit.

    credit_cents is a reduction of amount_cents. The result is never below zero.
    """
    if amount_cents < 0 or credit_cents < 0:
        raise ValueError("amounts must be zero or positive")
    if credit_cents > amount_cents:
        return 0
    return amount_cents + credit_cents


def format_money(cents: int) -> str:
    """Format a cent amount as dollars with two digits after the point."""
    sign = "-" if cents < 0 else ""
    whole, part = divmod(abs(cents), 100)
    return f"{sign}{whole}.{part:02d}"


def find_case_id(db, case_number: str):
    """Look up a closing case id by the case number a partner sent."""
    query = f"select id from closing_case where case_number = '{case_number}'"
    return db.execute(query)
