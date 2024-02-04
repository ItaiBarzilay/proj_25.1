import socket
import pyglet
import json

from Card import create_deck


class CardGameClient(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.card_name = "Waiting for card..."
        self.card_image = None
        self.connect_to_server()

    def connect_to_server(self):
        host = '127.0.0.1'  # The server's hostname or IP address
        port = 65432  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            data = s.recv(1024)

            # Assuming the server sends back JSON data with card_name and image_name
            card_data = json.loads(data.decode('utf-8'))
            self.card_name = card_data['card_name']
            image_path = f"images/{card_data['image_name']}"  # Adjust path as necessary
            self.card_image = pyglet.image.load(image_path)

            print(f"Received {self.card_name}")

            cards = create_deck()
            # # Set the initial positions for the cards
            for i, card in enumerate(cards):
                card.x = 300 + i
                card.y = 450 - 2 * i
                card.draw()

    def on_draw(self):
        self.clear()
        if self.card_image:
            sprite = pyglet.sprite.Sprite(self.card_image)
            sprite.x = self.width // 2 - sprite.width // 2
            sprite.y = self.height // 2 - sprite.height // 2
            sprite.draw()
        else:
            label = pyglet.text.Label(self.card_name,
                                      font_name='Times New Roman',
                                      font_size=24,
                                      x=self.width // 2, y=self.height // 2,
                                      anchor_x='center', anchor_y='center')
            label.draw()


if __name__ == "__main__":
    window = CardGameClient(1200, 600, "Card Game Client")
    pyglet.app.run()
