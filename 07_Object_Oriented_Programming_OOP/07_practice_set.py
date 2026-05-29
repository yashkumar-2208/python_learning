
#Ques_1: Create a class Car with a method drive() that prints "Car is moving".
#Create an object of Car and call drive().

class Car:

    def drive(self):
        print("Car is moving")

a = Car()
a.drive()


#Ques_2: Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
#Create an object and print the person’s name and age.


class Person:

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def person_info(self):
        print(f"The name is: {self.name} and age is: {self.age}")


a = Person("Jonh", 20)
a.person_info()


#Ques_3: Create a base class Animal with a method sound() that prints "Some sound".
#Create a derived class Dog that overrides sound() to print "Bark!".
#Create an object of Dog and call sound().


class Animal:

    def __init__(self, cat):
        self.cat = cat
    
    def print_sound(self):
        print("Meow")

a = Animal("Cat")
a.print_sound()


        
class Dog:

    def __init__(self, dog):
        self.dog = dog

    def print_sounds(self):
        print("Bark! ")

b = Dog("Sheru")
b.print_sounds()
        
