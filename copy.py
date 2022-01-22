import random
help(random.random)
exit()

# shallow and deep copy
# https://realpython.com/copying-python-objects/
import copy
def PrintInfo(a, b):
	print(a, b)
	if id(a) == id(b):
		print('ID is the same')
	else:
		print('ID is not the same')
	print('IS operation:', a is b)




# integer
a = 10
#b = copy.deepcopy(a)
#b = copy.copy(a)
b = a
PrintInfo(a, b)
a = 1
PrintInfo(a, b)
print('====')


# list
#c = [1, 2]
c = [[1, 1], [2, 2]] #
#d = copy.deepcopy(c)
d = copy.copy(c)
d = c
PrintInfo(c, d)
#c[0] = 3
#c[0][0] = 'A'
c[0] = ['A', 'B']
PrintInfo(c, d)
print('====')


# string
e = 'python'
#f = copy.deepcopy(e)
#f = copy.copy(e)
f = e
PrintInfo(e, f)
e = 'snake'
PrintInfo(e, f)
print('====')



# class 
class Car:
	def __init__(self, price):
		self.price = price
	def __str__(self):
		return str(self.price)
car1 = Car(100)
#car2 = copy.deepcopy(car1)
#car2 = copy.copy(car1)
car2 = car1
PrintInfo(car1, car2)
car1.price = 200
PrintInfo(car1, car2)