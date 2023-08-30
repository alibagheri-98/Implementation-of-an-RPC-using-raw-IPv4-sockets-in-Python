import os

from utils.socket_string_transfer import receive_bytes_from_socket, send_string_through_socket


class RPCReceiver:
    def __init__(self, server_name):
        self.server_name = server_name
        self.service_tenants = {}

    def _save_rpc(self, data):
        service_name = data['service_name']
        tenants = data['tenants']

        self.service_tenants[service_name] = tenants

        rpc_data = data['rpc']
        rpc_name = rpc_data['name']
        body = rpc_data['body']
        filename = f"{service_name}-{self.server_name}/{rpc_name}.py"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            # f.write("#" + json.dumps(rpc_data) + "\n")
            f.write(body)
        f.close()

    def retrieve_rpc_from_initializer_node(self, socket):
        import json
        switched_socket, switched_addr = socket.accept()

        while True:
            message = receive_bytes_from_socket(switched_socket)
            print(message)
            if message == "Done":
                break

            data = json.loads(message)
            self._save_rpc(data)
            send_string_through_socket(switched_socket, "Ok")

        switched_socket.close()
