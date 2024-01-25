import pyglet
import random


class Card(pyglet.sprite.Sprite):
    def __init__(self, card_name, image_name):
        full_image_path = f"images/{image_name}"
        image = pyglet.image.load(full_image_path)
        super(Card, self).__init__(image)

        self.card_name = card_name
        self.image_name = image_name

    def update_image(self):
        # self.image_name = f"{self.card_name}.png"
        # full_image_path = f"images/{self.image_name}"
        full_image_path = "images/card1.png"
        self.image = pyglet.image.load(full_image_path)

def generate_card_dict():
    suits = ["heart", "diamond", "club", "spade"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    dict_images = {}

    for suit in suits:
        for value in values:
            card_name = f"{suit}_{value}"
            image_name = f"card0.png"
            dict_images[card_name] = image_name

    return dict_images


def create_deck():
    dict_images = generate_card_dict()
    card_objects = [Card(card_name, image_name) for card_name, image_name in dict_images.items()]

    # Shuffle the deck
    random.shuffle(card_objects)

    return card_objects

#
# # Example usage:
# for card in deck:
#     print(f"Card Name: {card.card_name}, Image Name: {card.image_name}")
