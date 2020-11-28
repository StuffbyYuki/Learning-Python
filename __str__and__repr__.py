class Car:
	class_attr = 'class attribute'

	def __init__(self, name, make):
		self.name = name
		self.make = make

	def __str__(self):
		"""You can print on an instance of your class, used to print out stuff to users"""
		return f'__str__ called - Name: {self.name}, Make: {self.make}\n'

	def __repr__(self):
		"""This is similar to __str__ but for developers or debug purposes"""
		return f'__repr__ called - Name: {self.name}, Make: {self.make}\n'


car = Car('Civic', 'Honda')
print(car) # print() defaults to __str__ but not for __repr__
print(repr(car)) # you need to call repr() func for it to print, you can just to car in console to print it out though
print(str(car))  # you can of course call str() func as well



