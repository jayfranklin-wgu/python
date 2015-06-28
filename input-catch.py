#!/usr/bin/python

number = raw_input('Pick number between 1-10\n')

def TEST(arg):
		try:
				number = int(arg)
		except ValueError:
				print "Sorry {} is not a number." .format(arg)
		else:
				if 0 < number < 11:
						pass
				else:
						print '{} is out of range.'.format(arg)

		print "you entered {}!" .format(arg)
		return;
TEST(number)
