
def AskForNumber():
		while True:
				try:
						return int(input('Please enter a number: '))
				except ValueError:
						pass   # don't do this!
