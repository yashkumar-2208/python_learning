# Customize object creation and initialization (__init__, __new__).
# Enable operator overloading (e.g., +, -, *, ==, <, >).
# Provide string representations of objects (__str__, __repr__).
# Control attribute access (__getattr__, __setattr__, __delattr__).
# Make objects callable (__call__).
# Implement container-like behavior (__len__, __getitem__, __setitem__, __delitem__, __contains__).
# Support with context managers (__enter__,__exit__)


class Employee: 

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        a = f"The name is {self.name} and the salary is {self.salary}"
        print(a)

    def __repr__(self):
        a = f"name: {self.name}\nsalary: {self.salary}"
        print(a)

    def __len__(self):
        return len(self.name)

e1 = Employee("Tom", 2379)
e1.__str__()
e1.__repr__()
print(len(e1))