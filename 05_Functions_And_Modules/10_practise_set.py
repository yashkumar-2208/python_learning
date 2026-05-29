#Ques_1: Write a function greet() that prints "Hello, Python Learner!" when called.
def greet():
    print("Hello, Python Learner!")
greet()


#Ques_2:Write a function square(num) that returns the square of a given number. Test it with different numbers.
def square(num):
    c = num*num
    return c
print(square(5))

# Ques_3: Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

def calculate_area(length,width=10):
    c = 1/2 * length * width
    return c
print(calculate_area(length=20))


#Ques_4: Write a lambda function that adds two numbers and test it.
sum = lambda x,y: x+y
print(sum(x=2,y=4))


#Ques_5: Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

square = lambda x: x*x
list1 = [1, 2, 3, 4, 5]
print(list(map(square, list1)))


#Ques_6: Write a recursive function factorial(n) that returns the factorial of a number.
def factorial(n):
    if n == 0 or n ==1:
        return 1
    return factorial(n-1) * n
print(factorial(5))


#Ques_7: Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
def sum_of_digits(n):
    if n == 0 :
        return 0
    return n%10 + sum_of_digits(n//10)
print(sum_of_digits(7532))


#Ques_8: Import the math module and use it to:
# Find the square root of 144
# Calculate sin(90°) (hint: use math.radians())
import math #math module
print(math.sqrt(144))
print(math.radians(90))



#Ques_9: Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".
import requests
a = requests.get("https://api.github.com")
print(a.json())


#Ques_10: Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
def increment():
    counter = 1
    counter += 1
    print(counter)
increment()


#Ques_11: Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
def multiply(a,b):
    '''It gives the product of two numbers.'''
    a = int(input("Enter your 1st number: "))
    b = int(input("Enter your 2nd number: "))
    return a * b
print(multiply(2,2))
print(multiply.__doc__)



#Ques_12: Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.
def safe_divide(a,b):
    
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a/b

print(safe_divide(293,0))


#Ques_13: Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
import my_utils
print(my_utils.is_even())
















    
