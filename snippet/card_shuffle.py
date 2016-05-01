# Mission: Program a computer to shuffle a deck of cards

import itertools
import random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
print ('You got: {}'.format(deck[0:5])) # shuffle a deck of card randomly and deal 5 cards each time
