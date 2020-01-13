'''	Perry Kivolowitz
	Dealing cards
'''

import random

'''	Initialize a shuffled deck represented by a list
	of the integers 0 through 51 (inclusive) put in
	a random order.
'''

deck = list(range(52))
random.shuffle(deck)

'''	Reach into the deck N number of times (where N
	is, for example 5). For each integer retrieved,
	convert it from a number into a rank and suit.
	For example, if the card's value were 0, you 
	would build a string containing:

	Ace of Diamonds

	The choice of suit is up to you, of course.

	Remember, there are 4 suits and 13 ranks in each
	suit.
'''

cards_in_hand = 5
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

for card_index in range(cards_in_hand):
	card_string = ''
	card_value = deck[card_index]
	# Convert card_value to a rank and suit
	rank = card_value % 13
	suit = card_value // 13
	# Special case the "named" cards and for the others
	# simply use their numbers
	if rank == 0:
		card_string = 'Ace'
	elif rank == 10:
		card_string = 'Jack'
	elif rank == 11:
		card_string = 'Queen'
	elif rank == 12:
		card_string = 'King'
	else:
		card_string = str(rank + 1)

	card_string += ' of '
	card_string += suits[suit]

	print('{:d}. {:s}'.format(card_index + 1, card_string))
