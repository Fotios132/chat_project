
# Runs server that listens for incoming peer connections

import socket
import threading
import network

def start_server(port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("", port))

    server.listen()

    print(f"Listening on port {port}")

    while True:

        client, addr = server.accept()

        ip = addr[0]
        port = addr[1]

        network.connections.append((client, ip, port))

        print(f"\nConnected from {ip}:{port}")

        threading.Thread(
            target=network.receive_messages,
            args=(client, ip, port),
            daemon=True
        ).start()