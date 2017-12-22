def reducedproblem(first,second):
	edits = 0
	'''Recursively solves edit distance problem'''
	if len(first) == 0:
		return len(second)
	elif len(second) == 0:
		return len(first)
	elif first[0] == second[0]:
		return reducedproblem(first[1:],second[1:])
	else:
		addition = addletter(first,second)
		deletion = deleteletter(first,second)
		change = changeletter(first,second)
		return 1 + min(addition,deletion,change)

def addletter(first,second):
	return reducedproblem(first,second[1:])

def deleteletter(first,second):
	return reducedproblem(first[1:],second)

def changeletter(first,second):
	return reducedproblem(first[1:],second[1:])

print(reducedproblem("poems","spam"))
