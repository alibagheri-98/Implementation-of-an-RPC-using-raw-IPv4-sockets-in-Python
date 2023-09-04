# Implementation-of-an-RPC-using-raw-IPv4-sockets-in-Python
In this repository, a RPC is implemented using raw IPv4 sockets in Python. This project was my final project for the 'Data Networks' course instructed by Dr. Pakravan at Sharif University of Technology. For more informatino, read the "project_doc.pdf" file. The codes are "Codes" folder.
![1666937835556](https://github.com/alibagheri-98/Implementation-of-an-RPC-using-raw-IPv4-sockets-in-Python/assets/112773855/8bee0767-889d-4078-be8a-32ae642af6ea)

## Implementation
To implement RPC using raw IPv4 sockets in Python, you can follow these general steps:
1. Create a socket object using `socket.socket()`, specifying the socket type as `socket.SOCK_RAW`.
2. Bind the socket to a specific IP address and port.
3. Set the socket options to include IP headers.
4. Use the `sendto()` method to send data to the server.
5. Use the `recvfrom()` method to receive data from the server.
6. Parse the received data and handle it accordingly.

Note that raw sockets require bit-level modifications of less than 8 bit groups for writing the packet headers. Additionally, raw socket programming can be complex and requires a good understanding of networking protocols and low-level socket functions. It is recommended to use higher-level libraries or frameworks for implementing RPC, such as the `protobuf-socket-rpc` library. 

Overall, implementing RPC using raw IPv4 sockets in Python can be challenging, but it can provide more control and flexibility over the communication protocol.

## Advantages of Using Raw IPv4 Sockets for RPC Implementation in Python
Using raw IPv4 sockets for RPC implementation in Python can provide some advantages, such as:

1. Flexibility: Raw sockets allow for more control over the communication protocol, as they can be used to send any arbitrary binary data to any particular interface without any other details such as MAC address. This can be useful in cases where the communication protocol needs to be customized or optimized for specific requirements.

2. Bypassing TCP/IP processing: Raw sockets bypass the normal TCP/IP processing and send packets directly to the specific user application, which can be useful for receiving raw packets at the Ethernet layer. This can be beneficial in cases where the application needs to access lower-level protocols.

3. Low-level access: Raw sockets allow for direct access to lower-level protocols, which can be useful for applications that require bit-level modifications of less than 8 bit groups for writing the packet headers.

However, it is important to note that raw socket programming can be complex and requires a good understanding of networking protocols and low-level socket functions. Additionally, raw sockets require careful handling to ensure security and avoid potential vulnerabilities. It is recommended to use higher-level libraries or frameworks for implementing RPC, such as the `protobuf-socket-rpc` library. 

Overall, using raw IPv4 sockets for RPC implementation in Python can provide some advantages, but it requires careful consideration of the specific use case and a good understanding of networking protocols and low-level socket functions.

## Disadvantages of Using Raw IPv4 Sockets for RPC Implementation in Python
Using raw IPv4 sockets for RPC implementation in Python can also have some disadvantages, including:

1. Complexity: Raw socket programming can be complex and requires a good understanding of networking protocols and low-level socket functions. This can make it challenging for developers who are not familiar with low-level networking protocols.

2. Security: Raw sockets require careful handling to ensure security and avoid potential vulnerabilities. Improper use of raw sockets can lead to security issues such as denial-of-service attacks, packet injection, and packet sniffing.

3. Limited portability: Raw sockets are platform-dependent and may not be available on all operating systems. This can limit the portability of the application and make it difficult to deploy on different platforms.

4. Lack of error handling: Raw sockets do not provide error handling mechanisms, which can make it difficult to debug and troubleshoot issues.

5. Lack of standardization: Raw sockets do not follow any standard protocol, which can make it difficult to integrate with other systems and applications.

Overall, while using raw IPv4 sockets for RPC implementation in Python can provide some advantages, it also has some significant disadvantages. It is important to carefully consider the specific use case and weigh the pros and cons before deciding to use raw sockets for RPC implementation.
