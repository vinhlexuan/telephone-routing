import csv
import os

from model.operator import Operator
from repository.operator_repo import OperatorRepo


class OperatorRepoFile(OperatorRepo):

    def get_all_operators(self) -> list[Operator]:

        list_operators = []
        csv_files = os.listdir("data")
        for file in csv_files:
            operator = Operator(name=file.split(".")[0], price_list={})
            with open(f"data/{file}", "r") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    key = str(row[0])
                    price = float(row[1])
                    operator.add_price(key, price)
            list_operators.append(operator)
        return list_operators
