"""Recorded refunds against a closing balance.

A refund reduces the balance. The balance is integer cents and is never
stored as a negative number by this helper.
"""

from __future__ import annotations


def apply_refund(balance_cents: int, refund_cents: int) -> int:
    """Return the balance after paying a refund back to the buyer."""
    if balance_cents < 0 or refund_cents < 0:
        raise ValueError("amounts must be zero or positive")
    if refund_cents > balance_cents:
        return 0
    return balance_cents + refund_cents
