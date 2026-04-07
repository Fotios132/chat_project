

# Handles TCP connections, sending messages, and managing peers

import socket
import threading

connections = []

def get_my_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def connect_peer(ip, port, my_port):

    # prevent self connection
    if ip == get_my_ip() and port == my_port:
        print("Cannot connect to yourself")
        return

    # prevent duplicates
    for sock, conn_ip, conn_port in connections:
        if conn_ip == ip and conn_port == port:
            print("Duplicate connection")
            return

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))

        connections.append((sock, ip, port))

        print(f"Connected to {ip}:{port}")

        threading.Thread(
            target=receive_messages,
            args=(sock, ip, port),
            daemon=True
        ).start()

    except:
        print("Connection failed")


def list_connections():

    if not connections:
        print("No connections")
        return

    print("id: IP Address       Port")

    for i, conn in enumerate(connections):
        sock, ip, port = conn
        print(f"{i+1}: {ip:<15} {port}")


def terminate(conn_id):

    if conn_id < 1 or conn_id > len(connections):
        print("Invalid connection ID")
        return

    sock, ip, port = connections.pop(conn_id - 1)

    sock.close()

    print(f"Connection terminated: {ip}:{port}")


def send_message(conn_id, message):

    if len(message) > 100:
        print("Message too long (100 max)")
        return

    if conn_id < 1 or conn_id > len(connections):
        print("Invalid connection ID")
        return

    sock, ip, port = connections[conn_id - 1]

    try:
        sock.send(message.encode())
        print(f"Message sent to {conn_id}")

    except:
        print("Send failed")


def receive_messages(sock, ip, port):

    while True:

        try:
            data = sock.recv(1024)
            if not data:
                break

            message = data.decode()

            print(f"\nMessage received from {ip}")
            print(f"Sender's Port: {port}")
            print(f"Message: {message}\n")

        except:
            break

    print(f"Connection closed by {ip}")
    sock.close()

def exit_program():

    print("Closing all connections")

    for sock, ip, port in connections:
        sock.close()

    connections.clear()