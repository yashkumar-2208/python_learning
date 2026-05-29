def very_slow_func():
    print("Something......")
    return 70


a = very_slow_func()
if(very_slow_func()>10):
    print(very_slow_func())

else:
    print("It's not greater than 10")


print("----------------")

def count():
    print("Running")
    print("Running")
    print("Running")
    print("Running")
    return 7

if ((a:=very_slow_func())>10):
    print(a)

else:
    print("Not greater than 10")



print('------')

while (data:= input("Enter here: ")):
    print(f"You've entered: {data}")

    if data == "q":
        break
    else:
        continue