import sys

def Main():
	"""	Main() demonstrates executing the same code with and without handling
		potential exceptions.
	"""

	if len(sys.argv) < 2:
		print('Must supply a file name')
		exit(1)

	if input('Be safe? (y|n): ') == 'y':
		try:
			OpenAndProcessFile(sys.argv[1])
			print('OpenAndProcessFile() returned OK')
		except FileNotFoundError:
			print('Could not find:', sys.argv[1])
			exit(1)
	else:
		OpenAndProcessFile(sys.argv[1])
		print('OpenAndProcessFile() returned OK')
	exit(0)

def OpenAndProcessFile(filename):
	file = open(filename, 'r')
	print('File:', filename, 'opened.')
	file.close()

if __name__ == '__main__':
	Main()

def test_OpenFileAndProcess():
	try:
		# Unsafe open (that should fail).
		OpenAndProcessFile('ookokokokokokok')
		# We should not get here.
		assert(False)
	except FileNotFoundError:
		assert(True)