class RPCException(Exception):
    type = "RPC-EX"

    def __init__(self, ex_type, message=None):
        self.ex_type = ex_type
        self.message = message

    def __str__(self):
        return f"{self.ex_type}: {self.message}"
