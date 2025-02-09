# socket_config/client.py
import socket
from sockets.config import SERVER_IP, PORT, BUFFER_SIZE

def start_client():
    """Connects to the game server and handles moves."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    
    print(client.recv(BUFFER_SIZE).decode())  # Welcome message

    while True:
        try:
            move = input("Enter your move (e.g., e2e4): ")
            client.sendall(move.encode())

            # Wait for opponent's move
            move = client.recv(BUFFER_SIZE).decode()
            if not move:
                break

            print(f"Opponent moved: {move}")

        except:
            print("Disconnected from server.")
            break

    client.close()

if __name__ == "__main__":
    start_client()
