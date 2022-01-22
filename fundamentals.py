# fundamental operations/functions for Bool
# ==, <, <=, >, >=, !=
a = True
b = False
print('Converting True and False to integers gives 1 and 0:', int(True), int(False))




# fundamental operations/functions for numbers
# + - * /
print('Division always yields float:', 4/2)
# exponentiation: **
print('Return type of exponentiation depends on its inputs:', 2**2, 2**2.0)
# floor division: //
print('This gives 3 (return the integer part of the division):', 11//3)
# remainder (modulo): %
print('This gives 2:', 5%3)
# +=, -=, *=, /=, **=, //=, and %= are all valid abbreviation
a = 3
a += 2 # a = a + 2
a **= 2 # a = a**2
a %= 2 # a = a % 2
# abs
print('Absolute:', abs(2.1))
# min, max
print('Min and Max can take many inputs', min(2, 3, 5, 1), max(2, 3, 5, 1))
print('But one input will gives error:')
try:
	min(1)
except:
	print('Error!')
# round-up (四捨五入)
print('Round-up with specified number of digits (this returns 3.1416):', round(3.14159, 4))




# fundamental operations/functions for strings
# +
print('Summation will concatenate the string:', 'ABC' + 'DEF')
# *
print('Multiplication will repeats the string:', 2*'ABC')
# no -, /, //, and % operations for strings




# fundamental operations/functions for lists
# declaration
a = []
a = list()
a = list([1, 2, 3])
a = list((1, 2, 3))
# +
print('Summation will append the list:', [1, 2] + [3, 4])
# *
print('Multiplication will repeats the list:', 2*[1, 2])
# no -, /, //, and % operations for lists
# append: add one item to the list
a = [1, 2]
a.append(3)
print('Three items:', a)
# extend: add multiple itmes to the list
a = [1, 2]
a.extend((3, 4))
a.extend([5, 6])
print('Six items:', a)




# fundamental operations/functions for sets
# declariation
# a = {} this will create an empty dictionary, not set!
a = set()
a = {1, 2, 3}
a = set([1, 2, 3])
a = set((1, 2, 3))
# intersection:
b = {3, 4, 5}
print('Intersection between a and b:', a.intersection(b))
# union:
print('Union for a and b:', a.union(b))
# set minus operation -: a - b = a - a.intersection(b)
print(a - b)
# no plus operation +




# fundamental operations/functions for sets
# declariation
a = {}
a = {
	'Name' : 'John', 
	'Age' : 30, 
	'Color': 'yellow'
}
# referencing the value by key:
print('Age is:', a['Age'])
# add new key-value pairs:
a['Height'] = 170
print('New item in the dictionary:', a['Height'])
# delete key-value pairs:
del a['Height']
# number of key-value pairs in a dictionary:
print(len(a))
# create a 'view object' with all keys or values
# the objects will update itself when dictionary is modified
key_of_a= a.keys()
value_of_a = a.values()
print('Key and values before modification', key_of_a, value_of_a)
a['Weight'] = 80
print('Key and values after modification', key_of_a, value_of_a)
# the objects can be treated as iterables
print('List created from keys:', list(key_of_a))




# other fundamentals
# type: returns the type of the input
print('Integer, float, complex:', type(4), type(4.0), type(complex(1, 2)))


# del: 
"""
	removes object
	removes user-defined class
	removes items in lists according to index or slices
	removes key-value pairs in sets according to the key
"""
a = [1, 2, 3, 2, 1]
print('Before deletion:', a)
del a[1:3] # a is now [1, 2, 1]
print("After deletion:", a)
del a[:] # delete all items

class BB:
	b = "hello"
	print(b)
beta=BB
del BB
print(beta.b) # BB is deleted but class variables can be referred



# extra
# take an input from users (no effect when run on Sublime Text)
input_from_user = input('Please enter something:')
print('You have entered:')
print(input_from_user)
