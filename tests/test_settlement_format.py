from app.services.settlement import format_settlement_id


def test_format_settlement_id_pads():
    assert format_settlement_id(42) == "STL-000042"
