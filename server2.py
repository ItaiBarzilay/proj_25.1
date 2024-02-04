import socket
import threading
import json

from Card import create_deck

clients = [] #containing all server clients
nicknames = [] #containing all server nicknames

def handle_client(conn, addr, deck):
    print(f"Connected by {addr}")
    try:
        # Simulate sending a card to the player
        if deck:
            card = deck.pop(0)  # Remove a card from the deck
            card_data = {'card_name': card.card_name, 'image_name': card.image_name}
            message = json.dumps(card_data).encode('utf-8')  # Serialize card data to JSON and encode to bytes
            conn.sendall(message)
        else:
            print("Deck is empty.")
    finally:
        conn.close()


def start_server(host='127.0.0.1', port=65432):
    deck = create_deck()  # Create a deck of cards
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        for _ in range(3):
            conn, addr = s.accept()
            clients.append( (conn, addr) )

        for c in clients:
            client_thread = threading.Thread(target=handle_client, args=(c[0], c[1], deck))
            client_thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    start_server()
