import socket
from threading import Thread

from rcp_receiver import RPCReceiver
from rpc_managers import RPCManager
from utils.MessageModel import MessageAdapter
from utils.RPC_EX import RPCException
from utils.RPC_REQ import RPCREQAdapter, RPCREQ
from utils.RPC_RES import RPCRES
from utils.constants import RPCExceptionTypes
from utils.socket_string_transfer import receive_bytes_from_socket, send_string_through_socket


class Server:
    def __init__(self, server_name: str, ip: str, port: int) -> None:
        self.server_name = server_name
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(10)

        self.rpc_receiver = RPCReceiver(server_name)
        self.rpc_manager = RPCManager(server_name)

        # permissions
        self.service_tenants = {}

        # known clients
        self.clients = {"127.0.0.1": "c1"}

    def check_permission(self, client_name, service_name):
        if self.service_tenants.get(service_name, None) is None:
            return None
        if client_name not in self.service_tenants[service_name]:
            message = f"{client_name} does not have access to {service_name}!Be sure what are you asking!"
            raise RPCException(RPCExceptionTypes.ClientNotRegistered, message=message)

    def handle_client(self, switched_socket, switched_addr):
        response = None
        try:
            rpc_req_message = receive_bytes_from_socket(switched_socket)
            try:
                message = MessageAdapter.from_json(rpc_req_message)
            except:
                raise Exception("Not a request message!")
            if message.type != RPCREQ.type:
                raise Exception("Not a request message!")
            rpc_req = RPCREQAdapter(message.value)
            rpc_req.has_valid_argument_types()
            client_ip = switched_addr[0]
            client_name = self.clients[client_ip]
            self.check_permission(client_name, rpc_req.service_name)

            res = self.rpc_manager.handle_request(rpc_req)
            response = RPCRES(res)
        except RPCException as e:
            response = e
        except Exception as e:
            response = RPCException(RPCExceptionTypes.ExecutionException, message=f"{str(type(e))} -> {str(e)}")
        finally:
            message = MessageAdapter(response).to_json()
            send_string_through_socket(switched_socket, message)
            switched_socket.close()

    def serve_forever(self):
        print("waiting for initializer:")
        self.rpc_receiver.retrieve_rpc_from_initializer_node(self.server_socket)
        self.service_tenants = self.rpc_receiver.service_tenants

        print("start serving:")
        while True:
            switched_socket, switched_addr = self.server_socket.accept()
            t = Thread(target=self.handle_client, args=(switched_socket, switched_addr))
            t.setDaemon = True
            t.start()
