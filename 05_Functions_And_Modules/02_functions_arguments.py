def add(a,b):
    x = a+b
    return x

c = add(5,7)
print(c)

#default argumengts

def additional(a,b,plus=0):
    x = a+b+plus
    return x
y = additional(5,3,9)
print(y)

#keyword arguments

def student(name, age):
    print(f"Name: {name} and age: {age}")
student(name = "Yash", age=17)
