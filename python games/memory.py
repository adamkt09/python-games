# card game - memory

import simplegui
import random

# card deck
deck = []
exposed = []

card1 = 0
card2 = 0

state = 0
turns = 0

# function to initialize globals
def new_game():
    global deck, state, exposed, card1, card2, turns

    deck = list(range(10)) * 2
    random.shuffle(deck)

    exposed = [False] * len(deck)

    state = turns = card1 = card2 = 0

# define event handlers
def mouseclick(pos):
    global state, exposed, card1, card2, turns

    card_num = pos[0] // 50

    if not exposed[card_num]:
        exposed[card_num] = True

        if state == 0:
            state = 1
            card1 = card_num
        elif state == 1:
            state = 2
            card2 = card_num
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            if deck[card1] != deck[card2]:
                exposed[card1] = exposed[card2] = False
            card1 = card_num
            state = 1

# draw handler
def draw(canvas):
    for i, num in enumerate(deck):
        if exposed[i]:
            canvas.draw_text(str(num), [i * 50 + 10, 70], 50, "White")
        else:
            canvas.draw_polygon([(i * 50, 0), (i * 50, 100), ((i + 1) * 50, 100), ((i + 1) * 50, 0)], 1, "White", "Green")
    label.set_text("Turns = " + str(turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
