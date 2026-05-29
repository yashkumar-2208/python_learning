class Animal:

    def __init__(self,animal):
        self.amimal = animal

    def speak(self):
        print("Generic animal sound.")

a = Animal("Dog")
a.speak()


class Animal:
    location = "Australia"

    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        print("Speaking now...")
        

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!!")


d = Dog("Bruno")
d.speak()
# print(d.location)