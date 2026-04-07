
#Main program that handles user commands and starts the server thread

import sys
import select
import threading
import network
import server

is_running = True


def print_help():
    print("\nCommands:")
    print("help")
    print("myip")
    print("myport")
    print("connect <ip> <port>")
    print("list")
    print("terminate <connection id>")
    print("send <connection id> <message>")
    print("exit\n")


def thread_input(port):
    global is_running

    while is_running:

        command = input()
        parts = command.split()

        if not parts:
            continue

        action = parts[0]

        match action:

            case "help":
                print_help()

            case "myip":
                print(network.get_my_ip())

            case "myport":
                print(port)

            case "connect":
                if len(parts) != 3:
                    print("Usage: connect <ip> <port>")
                    continue
                try:
                    dest_port = int(parts[2])
                except ValueError:
                    print("Port must be a number")
                    continue
                network.connect_peer(parts[1], dest_port, port)

            case "list":
                network.list_connections()

            case "terminate":
                if len(parts) != 2:
                    print("Usage: terminate <id>")
                    continue
                try:
                    conn_id = int(parts[1])
                except ValueError:
                    print("Connection ID must be a number")
                    continue
                network.terminate(conn_id)

            case "send":
                if len(parts) < 3:
                    print("Usage: send <id> <message>")
                    continue
                try:
                    conn_id = int(parts[1])
                except ValueError:
                    print("Connection ID must be a number")
                    continue
                message = command.split(maxsplit=2)[2]
                network.send_message(conn_id, message)

            case "exit":
                is_running = False
                network.exit_program()
                break

            case _:
                print("Invalid command")


def main():
    if len(sys.argv) != 2:
        print("Usage: python chat.py <port>")
        sys.exit()

    port = int(sys.argv[1])

    # starting server thread
    server_thread = threading.Thread(
        target=server.start_server,
        args=(port,),
        daemon=True
    )

    server_thread.start()

    # start command input
    thread_input(port)


if __name__ == "__main__":
    main()