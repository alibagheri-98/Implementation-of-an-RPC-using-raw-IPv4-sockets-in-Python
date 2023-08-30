import json


class RPC:
    def __init__(self, name, arg_types, return_types, body) -> None:
        self.name = name
        self.arg_types = arg_types
        self.return_types = return_types
        self.body = body

    @classmethod
    def from_json(cls, message_as_bytes):
        return RPC(**json.loads(message_as_bytes.decode()))

    def to_json(self) -> bytes:
        return json.dumps(self.__dict__).encode()
