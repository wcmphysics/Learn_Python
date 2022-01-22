# remove
"""
	remove items according to values
	only remove the first match (searching from index 0)
	return None
	in-place
"""
a = [1, 2, 3, 2, 1]
a.remove(2)
print("Only first match is removed:", a)

a = [1, 2, 3, 2, 1]
print("Note that remove returns None:", a.remove(2))
print("Of course, a is modified", a)
del a
print('\n\n')




# pop()
"""
	remove items according to index (default to -1)
	return the removed item
	in-place (so the list pop applied to is also modified)
"""
a = [1, 2, 3, 2, 1]
print("Return the popped item", a.pop(-2))
print("Of course, a is modified", a)
del a
print('\n\n')




# sort()
"""
	sort the list in ascending order
	can sort the list according to results from a function applied to items
	return None
	in-place
"""
a = [1, 2, 3, 2, 1]
a.sort(reverse = True)
print("Reversely sorted list with number:", a)
b = ['z', 'a', 'f', 'b']
b.sort()
print("Sorted list with string:", b)
a = [1, -5, 3, -2, 1]
a.sort(key=abs, reverse = False)
print("Sorted list with function (note the values are not modified by the function):", a)
del a, b
print('\n\n')




# sorted()
"""
	sort the list in ascending order by default
	return the sorted list
	original list is not modified
"""
a = [1, 2, 3, 2, 1]
print("Sorted list:", sorted(a, reverse = True))
del a
print('\n\n')