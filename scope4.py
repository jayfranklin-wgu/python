myList = [1,2,3,4,5]

def work_on_list(some_list):
		working_copy = list(some_list)
		working_copy.append(10)
		return working_copy
		
		# this will return working_copy list and will not alter myList \
		#	because we used the list function to copy it to working_copy


# when i run this, it says TypeError: 'list' object is not callable

# troubleshoot later...
