import socket
import threading

AKIA6JVP4R6XTIWINKV5

def handle_client(client_socket, client_address):
    print(f"Connected client: {client_address}")

    while True:
        # Receive message from the client
        data = client_socket.recv(1024).decode("utf-8")

        if not data:
            # If the client disconnected, break the loop
            break

        print(f"Received message from {client_address}: {data}")

        # Echo the message back to the client
        client_socket.sendall(data.encode("utf-8"))

    # Close the client socket
    client_socket.close()
    print(f"Disconnected client: {client_address}")


def start_server():
    # Set the server host and port
    host = "127.0.0.1"  # localhost
    port = 5555

    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server started, waiting for connections...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()

        # Create a new thread to handle the client
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, client_address)
        )
        client_thread.start()


if __name__ == "__main__":
    start_server()

aws_access_key_id = AKIA6JVP4R6X6DGHBYU7
aws_secret_access_key = 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
