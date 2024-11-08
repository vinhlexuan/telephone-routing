class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.operator_price: dict[str, float] = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, operator: str, prefix: str, price: float):
        """
        Inserts a new operator with its price for a given prefix into the Trie.
        If the prefix already exists, it updates the price for the operator. 
        If not, it creates a new node with operator_price from its parent.
        Args:
            operator (str): The operator name.
            prefix (str): The prefix of the telephone number.
            price (float): The price associated with the operator.
        """
        node = self.root
        for digit in prefix:
            if digit not in node.children:
                new_child = TrieNode()
                new_child.operator_price = node.operator_price.copy()
                node.children[digit] = new_child
            node = node.children[digit]
        self._update_child_operator_dict(node, operator, price)

    def _update_child_operator_dict(self, node: TrieNode, operator: str, price: float):
        """
        Recursively updates the operator price dictionary for the given node and all its children.
        Args:
            node (TrieNode): The current node in the Trie.
            operator (str): The operator name.
            price (float): The price associated with the operator.
        """
        node.operator_price[operator] = price
        for child in node.children.values():
            self._update_child_operator_dict(child, operator, price)

    def search(self, telephone_number: str) -> dict[str, float]:
        node = self.root
        for digit in telephone_number:
            if digit not in node.children:
                break
            node = node.children[digit]
        return node.operator_price
