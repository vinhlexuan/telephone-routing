class Operator:
    def __init__(self, name: str, price_list: dict[str, float] = {}) -> None:
        self.name: str = name
        self.price_list: dict[str, float] = price_list

    def add_price(self, prefix: str, price: float) -> None:
        self.price_list[prefix] = price
        pass

    def sort_price_list(self) -> None:
        self.price_list = dict(
            sorted(self.price_list.items(), key=lambda x: x[0]))
        pass

    def __str__(self) -> str:
        return f"Operator: {self.name}, Price List: {self.price_list}"
