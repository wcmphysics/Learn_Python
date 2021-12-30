class Car:
	def __init__(self, brand, price):
		self.brand  = brand
		self.price = price
		self.slogan = f'This is a {self.price}-dollar car from {self.brand}!'

	def slogan_method(self):
		return f'This is a {self.price}-dollar car from {self.brand}!'

car1 = Car('BMW', 50000)

# Decorator (the concept of getter, setter, and deleter methods in java)
# allows for the access to a method like an attribute

# First, note that in the following the slogan doesn't change after brand is updated
print('--An example showing the problem--')
print(car1.slogan)
car1.brand = 'Porsch'
print(car1.slogan)

del car1
del Car

# a workaround for this is to remove the slogan attribute and define a method for slogan:
class Car:
	def __init__(self, brand, price):
		self.brand  = brand
		self.price = price
		#self.slogan = f'This is a {self.price}-dollar car from {self.brand}!'

	def slogan(self):
		return f'This is a {self.price}-dollar car from {self.brand}!'

car1 = Car('BMW', 50000)

print('--Using method--')
print(car1.slogan())
car1.brand = 'VW'
print(car1.slogan())

del car1
del Car


# but this would require changing 'slogan' to 'slogan()' in existing code
# with decorator, we can make slogan method behave like slogan attribute
class Car:
	def __init__(self, brand, price):
		self.brand  = brand
		self.price = price
		#self.slogan = f'This is a {self.price}-dollar car from {self.brand}!'

	@property 
	# this is 'getter': it gives values when slogan is refered like an attribute
	def slogan(self):
		return f'This is a {self.price}-dollar car from {self.brand}!'

	@slogan.setter 
	# this is 'setter': it describes what operations should be done when slogan is setted like an attribute 
	# note that setter can only take one argument
	# if you need many arguments, just put them into a tuple/list and pass it as one argument
	def slogan(self, brand_name):
		if brand_name == 'Volkswagen':
			self.brand = 'VW'
		else:
			print('!!Invalid brand_name!!')
			exit()

	@slogan.deleter 
	# this is 'setter': it describes what operations shall be done when slogan is deleted (using del) like an attribute
	# note that it takes no argument
	def slogan(self):
		print('Deletion is applied to slogan')
		self.brand = None
		self.price = None

car1 = Car('BMW', 50000)

# with @property (getter) we can get the slogan method like a property(note that no parentheses after slogan)
print('--Using decorator (getter)--')
print(car1.slogan)
car1.brand = 'Porsch'
print(car1.slogan)

# with @slogan.setter we can set things related to slogan as if slogan is an attribute
print('--Using decorator (setter)--')
print(car1.slogan)
car1.slogan = 'Volkswagen'
print(car1.slogan)

# with @slogan.deleter we can delete things related to slogan as if slogan is an attribute
print('--Using decorator (deleter)--')
print(car1.slogan)
del car1.slogan
print(car1.slogan)
