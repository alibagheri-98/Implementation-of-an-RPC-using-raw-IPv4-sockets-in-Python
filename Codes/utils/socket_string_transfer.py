def receive_bytes_from_socket(socket):
    len_message_byte = socket.recv(8)
    len_message = int.from_bytes(len_message_byte, "big")

    chunks = list()
    while True:
        chunks.append(socket.recv(8))
        if len(chunks) * 8 >= len_message:
            break

    message_byte = b''.join(chunks)
    message = message_byte[0:len_message].decode()
    return message


def send_string_through_socket(socket, message_str):
    l = len(message_str)
    socket.send(l.to_bytes(8, "big"))
    socket.send(message_str.encode())
