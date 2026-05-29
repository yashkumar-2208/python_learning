a = int(input("Enter your first number here: "))
b = int(input("Enter your second number here: "))

try:

    c = a/b
    print(c)
except Exception as e :
    print(e)
finally:
    print("Program executed sucessfully.")

