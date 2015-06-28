myList = [1,2,3,4,5]

def work_on_list(some_list):
		working_copy = some_list
		working_copy.append(10)
		return working_copy

# this will return [1,2,3,4,5,10], however myList will be altered.
