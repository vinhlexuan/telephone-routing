from dataclasses import dataclass


@dataclass
class Response:
    status: str
    message: str
    data: dict


class Success(Response):
    def __init__(self, message: str, data: dict):
        super().__init__("success", message, data)


class Invalid(Response):
    def __init__(self, message: str):
        super().__init__("invalid", message, {})


class NotFound(Response):
    def __init__(self, message: str):
        super().__init__("not_found", message, {})
