# io_module.py

import socket

def create_socket(host, port):
    """
    Create a new socket with the given host and port.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    return s

def listen_socket(s, backlog):
    """
Listen for incoming connections on the socket.
    """
    s.listen(backlog)

def accept_connection(s):
    """
    Accept an incoming connection on the socket.
    """
    connection, address = s.accept()
    return connection, address

def send_data(connection, data):
    """
    Send data over the connection.
    """
    connection.sendall(data.encode())

def receive_data(connection):
    """
    Receive data over the connection.
    """
    data = connection.recv(1024)
    return data.decode()

def close_connection(connection):
    """
    Close the connection.
    """
    connection.close()

# Example usage
host = "localhost"
port = 12345

s = create_socket(host, port)
listen_socket(s, 5)

while True:
    connection, address = accept_connection(s)
    print(f"Accepted connection from {address}")

    data = input("Enter data to send: ")
    send_data(connection, data)

    received_data = receive_data(connection)
    print(f"Received data: {received_data}")

    close_connection(connection)
