import socket
import threading

# Function to handle communication with a client
def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received from client: {data}")
            # Here you can add logic to process the received data (e.g., chess moves)
            response = input("Enter your response: ")
            client_socket.send(response.encode('utf-8'))
        except ConnectionResetError:
            break

    client_socket.close()

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  # Get the local machine name
    port = 5000  # Port to listen on

    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")
        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter the server's hostname or IP address: ")  # e.g., '192.168.1.2'
    port = 5000  # The same port as the server

    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {data}")

    client_socket.close()

