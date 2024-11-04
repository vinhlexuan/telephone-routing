from model.response import Invalid, NotFound, Response, Success
from model.trie import Trie
from repository.operator_repo import OperatorRepo


class TelephoneRouting:
    def __init__(self, operator_repo: OperatorRepo) -> None:
        self.trie: Trie = Trie()
        self.operator_repo: OperatorRepo = operator_repo
        self._load_operators_to_trie()

    def _load_operators_to_trie(self) -> None:
        operators = self.operator_repo.get_all_operators()
        for operator in operators:
            operator.sort_price_list()
            for prefix, price in operator.price_list.items():
                self.trie.insert(operator.name, prefix, price)

    def find_cheapest_operator(self, telephone_number: str) -> Response:
        if not self.validate_telephone_number(telephone_number):
            return Invalid(message="Invalid telephone number")
        operator_prices = self.trie.search(telephone_number)
        if not operator_prices:
            return NotFound(message="No operator supporting this telephone number")
        else:
            result_tupple = min(operator_prices.items(), key=lambda x: x[1])
            return Success(
                message="Cheapest operator found",
                data={"operator": result_tupple[0], "price": result_tupple[1]},
            )

    def validate_telephone_number(self, telephone_number: str) -> bool:
        return telephone_number.isdigit() and 0 < len(telephone_number)
