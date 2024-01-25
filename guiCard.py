import time

import pyglet

from Card import Card, create_deck

# Create a window
window = pyglet.window.Window(1200, 600)
width = window.get_size()[0]


cards =  create_deck()
# # Set the initial positions for the cards
for i, card in enumerate(cards):
    card.x = 300 + i
    card.y = 450 - 2 * i
    card.draw()


# # Define an update function for animation
def update(dt,place):
     cards[place].y -= 2  # Move the cards horizontally
     print(cards[place].y)
     if cards[place].y < 100:
         pyglet.clock.unschedule(update)  # Stop the update loop when all cards are gone


# Register the update function
x = -200
for i in range(0,3):
    pyglet.clock.schedule_interval(update, 1/100.0,i)
    cards[i].x = width/2 + x
    x+=200
    cards[i].update_image()



@window.event
def on_draw():
    window.clear()
    for card in cards:
        card.draw()

if __name__ == "__main__":
    pyglet.app.run()
