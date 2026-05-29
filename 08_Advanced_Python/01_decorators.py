def decorators(func):
    def wrapper():
        print("I'm about to execute a function.")
        func()
        print("I've executed a function.")
    return wrapper

def say_hello():
    print("Hello World! ")

f = decorators(say_hello)
f()

print("------")
def phone_specifications(func):

    def wrapper():
        print("Firstly phone name is: Iphone 17")

        func()
        print("Thirdly phone is working on A19 chip.")

    return wrapper


@decorators
def say_storage():
    print("Secondly the storage is 256gb. ")


#a = phone_specifications(say_storage)
#a()
say_storage()


#both methods works here.
