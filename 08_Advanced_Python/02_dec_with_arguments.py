#Decorators with arguments.py


def repeat(n):
    def decorators(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorators

@repeat(7)
def say_hello(a):
    print("Hello")
say_hello("hello")
    

print("--------")

def repeat(n):
    def decorators(func):
        def wrappers(a):
            for i in range(n):
                func(a)
        return wrappers
    return decorators

@repeat(10)
def say_hello(a):
    print(f"Hello {a}")
say_hello("Yash Kumar")


    
