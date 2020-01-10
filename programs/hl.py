import random

secret_number = random.randint(1, 128)
guess = -1
turn_counter = 0

'''	Loop until the user enters an integer that matches the previously
	chosen 'secret number'. Feedback is given to the user directing
	them to go higher or lower depending on the values in play.
'''

while guess != secret_number:
	guess = int(input('Guess a number from 1 to 128: '))
	turn_counter += 1
	if guess < secret_number:
		print('Higher')
	elif guess > secret_number:
		print('Lower')

print('You guessed it in', turn_counter, 'turns!')
