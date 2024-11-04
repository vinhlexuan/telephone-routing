import pytest
from unittest.mock import Mock

from model.operator import Operator
from model.response import Invalid, NotFound, Success
from repository.operator_repo import OperatorRepo
from service.telephone_routing import TelephoneRouting

@pytest.fixture
def mock_repo():
    return Mock(spec=OperatorRepo)

@pytest.fixture
def routing(mock_repo):
    return TelephoneRouting(mock_repo)

def test_find_cheapest_operator(routing, mock_repo):
    mock_repo.get_all_operators.return_value = [
        Operator(
            name="operator_a",
            price_list={
                "1": 0.9,
                "268": 5.1,
                "46": 0.17,
                "4620": 0.0,
                "468": 0.15,
                "4631": 0.15,
                "4673": 0.9,
                "46732": 1.1,
            },
        ),
        Operator(
            name="operator_b",
            price_list={"1": 0.92, "44": 0.5, "46": 0.2, "467": 1.0, "48": 1.2},
        ),
        Operator(
            name="operator_c",
            price_list={"1": 0.9, "44": 0.5, "46": 0.1, "467": 1.5, "48": 1.2},
        ),
    ]
    routing.load_operators_to_trie()
    result = routing.find_cheapest_operator("4673212345")
    assert result.data["operator"] == "operator_b"

def test_find_cheapest_operator_longest_prefix_match(routing, mock_repo):
    mock_repo.get_all_operators.return_value = [
        Operator(name="operator_a", price_list={"4673": 0.9, "46732": 1.1}),
        Operator(name="operator_b", price_list={"467": 1.5, "48": 1.2}),
        Operator(name="operator_c", price_list={"46": 1.4}),
    ]
    routing.load_operators_to_trie()
    result = routing.find_cheapest_operator("4673241321")
    assert result.data["operator"] == "operator_a"

def test_find_cheapest_operator_same_prefix(routing, mock_repo):
    mock_repo.get_all_operators.return_value = [
        Operator(name="operator_a", price_list={"467": 0.9, "235": 1.1}),
        Operator(name="operator_b", price_list={"467": 1.5, "235": 1.2}),
        Operator(name="operator_c", price_list={"467": 1.4, "235": 1.3}),
    ]
    routing.load_operators_to_trie()
    result = routing.find_cheapest_operator("235467")
    assert isinstance(result, Success)
    assert result.data["operator"] == "operator_a"

def test_find_cheapest_operator_no_match(routing, mock_repo):
    mock_repo.get_all_operators.return_value = [
        Operator(name="operator_a", price_list={"4673": 0.9, "46732": 1.1}),
        Operator(name="operator_b", price_list={"467": 1.5, "48": 1.2}),
        Operator(name="operator_c", price_list={"46": 1.4}),
    ]
    routing.load_operators_to_trie()
    result = routing.find_cheapest_operator("8976547")
    assert isinstance(result, NotFound)
    assert result.status == "not_found"

def test_find_cheapest_operator_empty_trie(routing):
    result = routing.find_cheapest_operator("1234567890")
    assert isinstance(result, NotFound)

def test_validate_phone_number(routing):
    assert routing.validate_telephone_number("1234567890") is True
    assert routing.validate_telephone_number("abc123") is False

def test_invalid_phone_number(routing):
    result = routing.find_cheapest_operator("abc123")
    assert isinstance(result, Invalid)

def test_empty_phone_number(routing):
    result = routing.find_cheapest_operator("")
    assert isinstance(result, Invalid)
