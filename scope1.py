x = 'Global'
def a():
		x = 'Local'
		print x
		
		# if x was not defined in the function and we try to print \
		#   the variable, Python will try to get the value from global \
		#	scope. This is called 'forward reference'.
		
		# if x is not defined in Global, then python will complain.
