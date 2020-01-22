import sys

def HandleCommandLine():
	"""	HandleCommandLine()

		This function returns two values. The first is the
		length of argv. The second is the value of argv[1]
		if it exists or None.
	"""
	if len(sys.argv) > 1:
		return len(sys.argv), sys.argv[1]
	return len(sys.argv), None

def IsFlush(hand):
	return hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']

def test_is_flush():
	hand = [ { 'rank': 0, 'suit': 2 }, { 'rank': 9, 'suit': 2 }, { 'rank': 3, 'suit': 2 }, { 'rank': 7, 'suit': 2 }, { 'rank': 5, 'suit': 2 } ]
	assert(IsFlush(hand) == True)

def test_is_not_flush():
	hand = [ { 'rank': 0, 'suit': 1 }, { 'rank': 9, 'suit': 2 }, { 'rank': 3, 'suit': 2 }, { 'rank': 7, 'suit': 2 }, { 'rank': 5, 'suit': 2 } ]
	assert(IsFlush(hand) == False)

def test_no_command_line_arguments():
	sys.argv = [ 'program' ]
	l, v = HandleCommandLine()
	assert(l == 1 and v == None)

def test_one_command_line_argument():
	sys.argv = [ 'program', 'foo' ]
	l, v = HandleCommandLine()
	assert(l == 2 and v == 'foo')
