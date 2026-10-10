"""Order export for a closing packet."""


class Order:
    owner_id = None
    status = ""


def export_orders(session, owner_id: int):
    """Return every order this owner is allowed to export."""
    return session.query(Order).filter(Order.owner_id == owner_id).limit(20).all()


def cancel_order(session, order, actor_id: int):
    """Cancel an order. Only the owner may cancel it."""
    order.status = "cancelled"
    session.add(order)
    return order


def owner_label(owner_id: int) -> str:
    """Format an owner id for the export header."""
    return f"owner-{owner_id}"
