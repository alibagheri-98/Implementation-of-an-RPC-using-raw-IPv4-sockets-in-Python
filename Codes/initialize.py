import json
import socket

from yaml import CLoader as Loader
from yaml import load

from utils.socket_string_transfer import send_string_through_socket, receive_bytes_from_socket


class InitialNode:
    def __init__(self):
        self.data = {}

    def start(self):
        print("start sending rcp...")
        self._load_data()
        self.send_rpc_to_all()

    def _load_data(self):
        self.data = load(open("./init.yaml"), Loader=Loader)

    def send_rpc_to_all(self):
        servers = self.data['network']['servers']
        for server in servers:
            server_name = list(server.keys())[0]
            server = server[server_name]
            ip = server['ip']
            port = server['port']
            self._send_rcp_to_server(server_name, ip, port)

    def _get_all_rpces(self):
        rpc_list = self.data['rpc']
        rpces = {}
        for rpc in rpc_list:
            rpc_name = list(rpc.keys())[0]
            rpc = rpc[rpc_name]
            with open(rpc['src']) as f:
                body = "".join(f.readlines())
            rpc['body'] = body
            rpc['name'] = rpc_name
            rpces[rpc_name] = rpc
        return rpces

    def _get_services(self):
        service_list = self.data['service']
        services = {}
        for service in service_list:
            service_name = list(service.keys())[0]
            service = service[service_name]

            services[service_name] = service
        return services

    def _send_rcp_to_server(self, server_name, ip, port):
        rpces = self._get_all_rpces()
        services = self._get_services()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((ip, port))
        for service_name in services:
            service = services[service_name]
            if server_name in service["providers"]:
                for rpc_name in service['rpcs']:
                    rpc = rpces[rpc_name]
                    message_data = {'rpc': rpc, 'tenants': service['tenants'], 'service_name': service_name}
                    message = json.dumps(message_data)
                    l = len(message)
                    client_socket.send(l.to_bytes(8, "big"))
                    client_socket.send(message.encode())
                    print(receive_bytes_from_socket(client_socket))
        send_string_through_socket(client_socket, "Done")
        client_socket.close()


initial_node = InitialNode()
initial_node.start()
