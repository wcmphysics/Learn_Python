# replace()
"""
	not in-place
"""

a = "a a a"
print('This replaces "a" with "b":', a.replace("a", "b")) # gives "b b b

a = "a a a"
print('This only replaces first 2 matches', a.replace("a", "b", 2)) # gives "b b a"



# find()
"""
	find the index of first match
	return -1 when no match
"""
a = "1234"
print('The substring "23" is found at:', a.find("23"))



# isalpha(), isalnum(), isupper(), islower()
"""
	determine if all of characters in a string are alphabets(including both upper and lower cases),
	alphabets or numbers, upper case alphabets, lower case alphabets
"""
a = "aab"
print("This string is alphabetic:", a.isalpha())




# translate()
"""
	https://www.w3schools.com/python/ref_string_translate.asp
"""