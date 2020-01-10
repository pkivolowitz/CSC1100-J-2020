import random
import math

print('*** Using randomly thrown \'darts\' to approximate PI ***')
number_of_trials = int(input('Enter number of trials (zero or negative value exits): '))
number_of_hits = 0
trial_counter = 0

while trial_counter < number_of_trials:
	trial_counter += 1
	x,y = random.random(), random.random()
	if math.sqrt(x * x + y * y) < 1:
		number_of_hits += 1

print('Throwing', number_of_trials, 'darts at a unit square landed within a distance of 1', number_of_hits, 'times.')
print('This gives an approximate value of PI of:', 4 * number_of_hits / number_of_trials)
