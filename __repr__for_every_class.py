# __repr__ is to help developers for debugging purposes
# You should have __repr__ for a class you're building
# The result of __str__ should be readable. The result of __repr__ should be unambiguous

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__, 
            self.first_name, self.last_name)
         

p = Person('Bob', 'Smith')
print(repr(p))


