import pytest
from model.trie import Trie


@pytest.fixture
def trie():
    return Trie()


def test_insert(trie):
    trie.insert("operator_a", "46", 0.9)
    trie.insert("operator_b", "4673", 1.0)

    assert (
        trie.root.children["4"]
        .children["6"]
        .children["7"]
        .children["3"]
        .operator_price["operator_a"]
        == 0.9
    )
    assert set(
        trie.root.children["4"]
        .children["6"]
        .children["7"]
        .children["3"]
        .operator_price.keys()
    ) == {"operator_a", "operator_b"}


def test_search(trie):
    trie.insert("operator_a", "46", 0.9)
    trie.insert("operator_b", "4673", 1.0)

    result = trie.search("4673")
    assert result == {"operator_a": 0.9, "operator_b": 1.0}
    result = trie.search("467")
    assert result == {"operator_a": 0.9}


def test_multiple_operators(trie):
    trie.insert("operator_a", "46", 0.9)
    trie.insert("operator_b", "467", 1.0)
    trie.insert("operator_c", "4673", 0.8)

    result = trie.search("4673")
    assert result == {"operator_a": 0.9, "operator_b": 1.0, "operator_c": 0.8}


def test_no_match(trie):
    trie.insert("operator_a", "46", 0.9)
    result = trie.search("1")
    assert result == {}
