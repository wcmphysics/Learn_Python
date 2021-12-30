
# remove
"""
	in-place
	only remove the first match
	return None
"""
a = [1, 2, 3, 2, 1]
a.remove(2)
print("Only first match is removed:", a)

a = [1, 2, 3, 2, 1]
print("Note that remove returns None:", a.remove(2))
print("Of course, a is modified", a)




# pop()
"""
	https://www.programiz.com/python-programming/methods/list/pop
"""