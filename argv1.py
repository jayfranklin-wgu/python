#!/usr/bin/python

import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]

print "the name of the script is {}".format(sys.argv[0])

try: 
		print int(arg1) + int(arg2)

except ValueError:
		print "you didnt give me a number"
