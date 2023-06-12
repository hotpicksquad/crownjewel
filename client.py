import socket

def start_client():
    # Set the server host and port
    host = "127.0.0.1"  # localhost
    port = 5555

    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")

    while True:
        # Prompt the user to enter a message
        message = input("Enter a message (or 'q' to quit): ")

        if message == "q":
            # If the user enters 'q', close the client socket and break the loop
            client_socket.close()
            break

        # Send the message to the server
        client_socket.sendall(message.encode("utf-8"))

        # Receive the echoed message from the server
        data = client_socket.recv(1024).decode("utf-8")

        print(f"Received message from the server: {data}")

if __name__ == "__main__":
    start_client()
