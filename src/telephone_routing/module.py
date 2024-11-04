from repository.impl.operator_repo_file import OperatorRepoFile
from repository.operator_repo import OperatorRepo
from service.telephone_routing import TelephoneRouting


class Module:
    def __init__(self):
        self.repository: OperatorRepo = OperatorRepoFile()
        self.routing_service = TelephoneRouting(self.repository)
