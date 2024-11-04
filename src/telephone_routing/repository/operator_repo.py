from typing import Protocol

from model.operator import Operator


class OperatorRepo(Protocol):
    def get_all_operators(self) -> list[Operator]: ...
