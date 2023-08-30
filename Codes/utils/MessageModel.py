import json


class Message:
    def __init__(self, type: str, value: str) -> None:
        self.type = type
        self.value = value

    @classmethod
    def from_json(cls, message_string):
        return Message(**json.loads(message_string))

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


class MessageAdapter(Message):
    def __init__(self, m):
        super(MessageAdapter, self).__init__(m.type, str(m))
