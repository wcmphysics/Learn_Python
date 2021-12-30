class Car:

	# this is class variable, which will be shared for all instances of the same class
	discount = 0.1
	number_of_car = 0

	# this __init__ describe what are executed when an instance of the class is created
	# first variable is always the instance itself, and is named 'self' by convention
	def __init__(self, brand, price):
		# these are attributes that is specific to an instance
		self.brand  = brand
		self.price = price
		self.slogan = f'This is a {self.price}-dollar car from {self.brand}!'
		# note that below it is 'Car.discount' rather than just 'discount'
		# class variables should be accessed through the class name
		Car.number_of_car += 1

	# a method (namely, a function) of the class
	def ApplyDiscount(self):
		#self.price = int(self.price*(1 - Car.discount)) 
		# you can also assess the class variable through the instance of the class
		# note that this allows one to override the value of dicount of the class
		# so you can assign an instance-dependent discount
		# and if you didn't assign an instance-dependent discount, it will just be the class variable (due to resolution priority)
		self.price = int(self.price*(1 - self.discount)) 

	# a class method: the method that operates on a class rather than an instance of a class
	# note that the the first element of the method is now a class and is named 'cls' by convention
	@classmethod
	def SetDiscount(cls, discount):
		cls.discount = discount

	# a common usage of class method: an alternative constuctor for a class
	# for example: create an instance of the class Car by reading in a string of the form 'brand-price'
	@classmethod
	def CreatedFromString(cls, car_string):
		brand, price = car_string.split('-')
		return cls(brand, price)

	# a static method: a method that use no info from an instance or the class 
	# an easy way to see if a method could be static is to see if 'self' or 'cls' doesn't appear at all
	@staticmethod
	def IsFast(TopSpeed): # the first element is no longer an instance or a class
		if TopSpeed >= 100:
			return True
		return False

	# this __repr is a special method related to the operation for print
	# by convention, this should yield valid python assignment code to the instance
	# see the name of other special methods at: https://docs.python.org/3/reference/datamodel.html#special-method-names
	# the double underlines are called "dunder"
	def __repr__(self):
		# you can copy the return of this directly to python code for recreating the instance
		return f"Car('{self.brand}', {self.price})"

	# this __str__ is another special method related to the operation for print
	# it has higher priority than __repr__ when invoking print
	def __str__(self):
		return f'Brand: {self.brand}\nPrice: {self.price}\nSlogan: {self.slogan}'

	# this is a special method handling operation of plus sign '+'
	# self => argument on the left of +
	# other => argument on the right of +
	# in this example we define the + operation as summation of the price of the two cars
	def __add__(self, other):
		return self.price + other.price


# creating instances of a class
car1 = Car('BMW', 50000)
car2 = Car('Benz', 40000)

# you can also add more attributes to an instance of a class directly
car1.color = 'red'
print(car1.color)
# python first look into __init__ for the attribute dicount. If not found, go search the variable 'discount' in the class.
print(car1.discount) 
# this is the variable 'discount' of the class
print(Car.discount)
# here car2 has the attribute discount so python doesn't return the discount in the class.
car2.discount = 0.2
print(car2.discount)
# show the name space of an object to see what content the object has
print(car1.__dict__)


# apply a method to an instance of the class
# note that for method => with parentheses; attribute => no parentheses
print(car1.price)
car1.ApplyDiscount()
print(car1.price)

# applying class method to a class
print(Car.discount)
Car.SetDiscount(0.25)
print(Car.discount)

# example for using class method for constructing an instance of the class
string3 = 'Toyota-30000'
car3 = Car.CreatedFromString(string3)
print(car3)

# an example of a static metehod
print(Car.IsFast(150))

# example for special methods for a class
# note that printing car1 no longer returns object name and memory address
print(car1)
print(car1.__repr__())
print(car1.__str__())

# another example of special method (add price of two cars)
print(car1.price, car2.price)
print(car1 + car2)




# inheritance of class: RaceCar will inherit all attributes and methods from the class Car.
# RaceCar is considered as a child class or a subclass of the parent class Car
# With this, one can build related classes efficiently
class RaceCar(Car):

	# note that discout appears in both RaceCar and Car
	# and the one in RaceCar will be referenced first when refering RaceCar.discount
	# all of the referencing orders for methods/attributes/variables are shown by invoking help(object_in_question)
	discount = 0.01 
	#number_of_car = 0

	def __init__(self, brand, price, TimeTo100KM):
		# specifying the operations for some variables to those in the parent class
		# so 'brand' and 'price' will be handled acoording to the __init__ in the class Car
		super().__init__(brand, price)
		# another way to do the above is (may only work in one-layer subclass):
		#Car.__init__(self, brand, price)
		self.TimeTo100KM = TimeTo100KM




# initiate an instance of a child class, with an additional item TimeTo100KM
car4 = RaceCar('Porsch', 90000, 10)

# 'help' is very helpful when observing the priority of calling an attribute or method
# it also gives what methods and attributes are allowed for the object
print(help(car4))

# note that ApplyDiscount first looks for discount in RaceCar(and then the discount in Car if not found)
print(car4.price)
car4.ApplyDiscount()
print(car4.price)

# to see if an object belongs to a class (or a parent class)
print(isinstance(car4, Car))
print(isinstance(car4, RaceCar))

# to see if a class is a subclass of a class
print(issubclass(RaceCar, Car))










				



	

