# socket_config/server.py
import socket
import threading
from sockets.config import SERVER_IP, PORT, BUFFER_SIZE

def handle_client(conn1, conn2):
    """Relays moves between two players."""
    turn = conn1  # Player 1 starts
    while True:
        try:
            move = turn.recv(BUFFER_SIZE).decode()
            if not move:
                break

            print(f"Move received: {move}")

            # Send move to opponent
            opponent = conn2 if turn == conn1 else conn1
            opponent.sendall(move.encode())

            # Switch turns
            turn = opponent
        except:
            print("Connection lost.")
            break

    conn1.close()
    conn2.close()

def start_server():
    """Starts the game server and listens for two clients."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, PORT))
    server.listen(2)
    print(f"Server started on {SERVER_IP}:{PORT}. Waiting for players...")

    conn1, addr1 = server.accept()
    print(f"Player 1 connected from {addr1}")
    conn1.sendall(b"Welcome Player 1. Waiting for Player 2...")

    conn2, addr2 = server.accept()
    print(f"Player 2 connected from {addr2}")
    conn2.sendall(b"Welcome Player 2. Game starting...")

    conn1.sendall(b"Game Start. You are White.")
    conn2.sendall(b"Game Start. You are Black.")

    # Start handling the game in a separate thread
    threading.Thread(target=handle_client, args=(conn1, conn2)).start()

# if __name__ == "__main__":
#     start_server()
