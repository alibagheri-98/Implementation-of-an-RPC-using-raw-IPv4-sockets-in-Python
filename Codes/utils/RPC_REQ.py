from utils.RPC_EX import RPCException
from utils.constants import ArgumentType, RPCExceptionTypes


class RPCREQ:
    type = "RPC-REQ"

    def __init__(self, service_name, rpc_name, arguments, argument_types, return_types):
        self.service_name = service_name
        self.rpc_name = rpc_name
        self.arguments = arguments
        self.argument_types = argument_types
        self.return_types = return_types

    def has_valid_argument_types(self):
        if len(self.arguments) != len(self.argument_types):
            message = f"Your arguments were: {self.arguments}"
            message += f"But expected arguments are {self.argument_types}"
            message += f"with return type: {self.return_types}"
            raise RPCException(RPCExceptionTypes.InvalidArguments, message=message)
        for i in range(len(self.argument_types)):
            arg_type = self.argument_types[i]
            arg = self.arguments[i]
            valid = ArgumentType.type_validator(arg_type, arg)
            if not valid:
                message = f"Expected type {arg_type} in position {i + 1} but {arg} were provided!"
                raise RPCException(RPCExceptionTypes.InvalidArguments, message=message)
        return True

    def __str__(self):
        res = f"{self.service_name}|{self.rpc_name}|"
        for arg in self.arguments:
            res += f"{arg}|"
        for arg_type in self.argument_types:
            res += f"{arg_type}|"
        res += f"{self.return_types}"


class RPCREQAdapter(RPCREQ):
    def __init__(self, data_string):
        self.data_string = data_string
        data_parts = data_string.split("|")
        service_name = data_parts.pop(0)
        rpc_name = data_parts.pop(0)
        return_types = data_parts.pop(-1)
        arguments_length = len(data_parts) // 2
        arguments = data_parts[:arguments_length]
        argument_types = data_parts[arguments_length:]

        super().__init__(service_name, rpc_name, arguments, argument_types, return_types)
