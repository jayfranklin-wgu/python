#!/usr/bin/python

import random
import sys

# Generate random integer between range of 0 and 10.
random_num = random.randint(0, 10)

""" Debug code
print str(random_num) + "\n\n\n"
"""

print "Random Number Guess!"

print "Pick a number between 0 and 10."
print "I will let you know if you guessed it!"
		
answer = 0

def user():
		global answer 
		answer = raw_input("Please enter a number between 0 and 10\n")
		IsValidNumber(answer)
		#print random_num
		#print '{}'.format(answer)
		if int(answer) < random_num:
				print 'Too low. try again!'
				user()
		elif int(answer) > random_num:
				print 'Too high! try again!'
				user()
		else:
				print "You got it!"
		return answer;

def IsValidNumber(arg):
		# print '{}'.format(arg)
		try:
			number = int(arg)
		except ValueError:
				print 'Sorry {} is not a number.' .format(arg)
				print 'Exiting...'
				sys.exit(1)
		else:
				if 0 < number < 11: 
						pass
				else:
						print '{} is out of range.'.format(arg)
		return arg;

user()

print 'You entered {}!'.format(answer)
