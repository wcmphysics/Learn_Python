

# map(function, iter)
"""
	Returns an iterator.
"""

a = [1.11, 2.22, 3.33]
map_object = map(int, a) # this map object is an iterator
print("This maps the input iterable according to the function specifed:", list(map_object))
print("The function is flexible. Here floats are mapped to strings:", list(map(str, a)))

def MySquareFunction(MyInput):
	return MyInput*MyInput
a = [1, 2, 3]
print("We can define the mapping function:", list(map(MySquareFunction, a)))
print("lambda is generally used for simple functions:", list( map(lambda x: x*x, a) ))

a = [1, 2, 3]
b = [4, 5, 6]
print("Can take more than one iterables:", list(map(lambda x, y: x*y, a, b)))


# in
"""
	https://stackabuse.com/python-check-if-string-contains-substring/
"""



# enumerate
"""
	https://www.geeksforgeeks.org/enumerate-in-python/
"""



# next
"""
	https://www.programiz.com/python-programming/methods/built-in/next
"""
           
        
    