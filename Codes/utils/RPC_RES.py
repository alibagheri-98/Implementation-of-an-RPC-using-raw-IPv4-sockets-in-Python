class RPCRES:
    type = "RPC-RES"

    def __init__(self, return_values):
        self.return_values = return_values

    def __str__(self):
        return f"{self.return_values}"
