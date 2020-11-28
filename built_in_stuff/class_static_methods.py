class Car:
	class_attr = 'class attribute'

	def __init__(self, name, make):
		self.name = name
		self.make = make

	def instance_method(self):
		return f'This is just a method, having access to states and attributes of an instance: {self.name}, {self.make}'

	@classmethod
	def class_method(cls):
		return f'This is class method and accessing {cls.class_attr}'

	@staticmethod
	def static_method():
		return f'This is static method and this just belongs to the class'

car = Car('Civic', 'Honda')
print(car.instance_method()) 
print(Car.instance_method(car)) # above line can be called like this
print(car.class_attr) # an instance of a class can of course use class attributes 
print(Car.class_method()) # class methods can be called on Car class and have access to class attributes / states
print(Car.static_method()) # static methods can be called on Car class; just belongs to the class


