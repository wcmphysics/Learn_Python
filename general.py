
# del
"""
	delete any object (variables, strings, lists, sets, and classes)
	item inside them can also be deleted (not sure for classes)

"""
a = [11, 12, 13]
print(a)
del a[1]
print(a)

class BB:
	b = "hello"
	print(b)

beta=BB
del BB
print(beta.b) # BB is deleted but class variables can be referred

