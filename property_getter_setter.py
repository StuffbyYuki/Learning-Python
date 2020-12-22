class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age < self._age:
            print('Enter a valid age.')
        else:
            self._age = new_age
    
    @age.deleter
    def age(self):
        del self._age

p = Person('Bob', 'Smith', 26)
print('Default age: ', p.age)
p.age = 30
print('Updated age: ', p.age)
del p.age
print('Should thrown an error: ')
try:
    p.age
except AttributeError as e:
    print(e)


    

