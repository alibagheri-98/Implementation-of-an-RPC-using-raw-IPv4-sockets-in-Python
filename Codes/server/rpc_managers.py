import os

from utils.RPC_EX import RPCException
from utils.RPC_REQ import RPCREQ
from utils.constants import RPCExceptionTypes
from utils.load_script import load_module_from_script_file


class RPCManager:
    def __init__(self, server_name):
        self.server_name = server_name

    def handle_request(self, rpc_req: RPCREQ):
        service_folder_path = f"{rpc_req.service_name}-{self.server_name}"
        file_name = f"{rpc_req.rpc_name}.py"
        path = f"{service_folder_path}\\{file_name}"
        if not os.path.isdir(service_folder_path):
            raise RPCException(RPCExceptionTypes.ServiceNotFound)
        if not os.path.exists(path):
            raise RPCException(RPCExceptionTypes.RPCNotFound)

        func = load_module_from_script_file(path, rpc_req.rpc_name)
        return func(*[eval(arg) for arg in rpc_req.arguments])
