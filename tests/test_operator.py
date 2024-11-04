import pytest
from src.telephone_routing.model.operator import Operator


@pytest.fixture
def mock_operator():
    return Operator(
        name="test_operator",
        price_list={
            "46": 0.17,
            "268": 5.1,
            "468": 0.15,
            "1": 0.9,
            "4631": 0.15,
            "4673": 0.9,
            "4620": 0.0,
            "46732": 1.1,
        },
    )


def test_sort_price_list(mock_operator):
    mock_operator.sort_price_list()
    sorted_price_list = list(mock_operator.price_list.items())
    expected_order = [
        ("1", 0.9),
        ("268", 5.1),
        ("46", 0.17),
        ("4620", 0.0),
        ("4631", 0.15),
        ("4673", 0.9),
        ("46732", 1.1),
        ("468", 0.15),
    ]
    assert sorted_price_list == expected_order
