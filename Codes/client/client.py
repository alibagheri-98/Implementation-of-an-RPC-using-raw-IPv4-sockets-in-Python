import socket

from utils.MessageModel import Message
from utils.RPC_REQ import RPCREQ
from utils.socket_string_transfer import send_string_through_socket, receive_bytes_from_socket


class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def do_req(self, req):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.server_ip, self.server_port))
        print("#################")
        print(req)
        message = Message(RPCREQ.type, req)
        send_string_through_socket(client_socket, message.to_json())
        print(receive_bytes_from_socket(client_socket))

        client_socket.close()


client = Client("127.0.0.1", 8000)
client.do_req("service1|rpc1|7|int|int")
client.do_req("service2|rpc1|7|int|int")
client.do_req("service3|rpc1|7|int|int")
client.do_req("service1|rpc2|7|int|int")
client.do_req("service1|rpc3|7|int|int")
client.do_req("service1|rpc1|7|str|int")
