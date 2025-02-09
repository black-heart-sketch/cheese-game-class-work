# main.py
import sys
from sockets.server import start_server
from sockets.client import start_client
# from chess.game import ChessGame  # Import your existing chess logic

def main():
    print("Choose an option:")
    print("1. Start Server")
    print("2. Connect as Client")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        start_server()
    elif choice == "2":
        start_client()
    else:
        print("Invalid choice. Exiting.")
        sys.exit()

if __name__ == "__main__":
    main()
