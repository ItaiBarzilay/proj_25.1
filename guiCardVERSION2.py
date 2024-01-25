import time

import pyglet

from Card import Card, create_deck

# Create a window
window = pyglet.window.Window(1200, 600)
width = window.get_size()[0]

cards = create_deck()
# # Set the initial positions for the cards
for i, card in enumerate(cards):
    card.x = 300 + i
    card.y = 450 - 2 * i
    card.draw()


# # Define an update function for animation
def update(dt, place):
    cards[place].y -= 2  # Move the cards horizontally
    print(cards[place].y)
    if cards[place].y < 100:
        pyglet.clock.unschedule(update)  # Stop the update loop when all cards are gone


# Register the update function
x = -200
for i in range(0, 3):
    pyglet.clock.schedule_interval(update, 1 / 100.0, i)
    cards[i].x = width / 2 + x
    x += 200
    cards[i].update_image()


def create_popup_window():
    popup_window = pyglet.window.Window(300, 100, caption="Continue?")
    layout = pyglet.text.Label(
        'Do you want to continue?',
        font_size=18,
        x=popup_window.width // 2, y=popup_window.height - 30,
        anchor_x='center', anchor_y='center'
    )
    yes_button = pyglet.text.Label(
        'YES',
        font_size=18,
        x=popup_window.width // 4, y=20,
        anchor_x='center', anchor_y='center',
        color=(0, 255, 0, 255)
    )
    no_button = pyglet.text.Label(
        'NO',
        font_size=18,
        x=popup_window.width * 3 // 4, y=20,
        anchor_x='center', anchor_y='center',
        color=(255, 0, 0, 255)
    )

    @popup_window.event
    def on_draw():
        popup_window.clear()
        layout.draw()
        yes_button.draw()
        no_button.draw()

    @popup_window.event
    def on_mouse_press(x, y, button, modifiers):
        if yes_button.x - yes_button.content_width // 2 < x < yes_button.x + yes_button.content_width // 2 \
                and yes_button.y - yes_button.content_height // 2 < y < yes_button.y + yes_button.content_height // 2:
            popup_window.close()
            return True  # Player selected YES
        elif no_button.x - no_button.content_width // 2 < x < no_button.x + no_button.content_width // 2 \
                and no_button.y - no_button.content_height // 2 < y < no_button.y + no_button.content_height // 2:
            popup_window.close()
            return False  # Player selected NO

    return popup_window


def game_loop(dt):
    global cards

    # ... (Your existing code)

    # Check if the player wants to continue
    popup_window = create_popup_window()
    pyglet.app.run()
    player_choice = None
    while player_choice is None:
        player_choice = popup_window.dispatch_events()

    if player_choice:
        print("Player chose to continue.")
        # Continue the game, add more cards, etc.
    else:
        print("Player chose to stop.")
        pyglet.app.exit()


@window.event
def on_draw():
    window.clear()
    for card in cards:
        card.draw()


if __name__ == "__main__":
    pyglet.app.run()
    game_loop()
