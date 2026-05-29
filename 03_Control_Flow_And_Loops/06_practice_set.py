#Ques1: Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

while True:
    user = int(input("Enter a number here: "))
    if user >= 1:
        print("It's a positive number.")
    elif user == 0:
        print("It's a zero.")
    elif user <=1:
        print("It's a negative number.")
    else:
        print("Enter valid input!")


#Ques_2: Create a program that checks if a person is eligible to vote (age >= 18).

while True:
    age = int(input("Enter your age here: "))
    if age == 18:
        print("Yes now you're eligible to vote, let's make your voting id.")
    elif age >=18:
        print("Yes you're eligible to give vote to your favourable party.")
    elif age == 0:
        print("You're not born yet!")
    elif age <=18:
        print("You're not eligible to vote vote until you turn 18.")
    else:
        print("Invalid age or input.")


#Ques_3: Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

while True:
    user = int(input("Enter any number here: "))
    if (user % 2 ==0) :
        print("It's a even number")
    else:
        print("It's a odd number")


#Ques_4: Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

user = int(input("Enter number from (1-7) to know about day of the week: "))

match user:

    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")



#Ques_5: Write a program using match case that simulates a simple calculator.
#Ask the user for two numbers and an operation (+, -, *, /).
#Perform the operation using match case.

while True:
    a  = int(input("Enter your first number here: "))
    b = int(input("Enter yout second number here: "))
    user = input("Enter an arithmetic here (+, -, *, /): ")

    match user:
        case "+":
            print("a + b =",a+b)
        case "-":
            print("a - b =",a-b)
        case "*":
            print("a * b =",a*b)
        case "/":
            print("a / b =",a/b)
        case _:
            print("Invalid operation.")


#Ques_6: Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#Ques_7: Print the multiplication table of a number (entered by user).

user = int(input("Enter number which you want it's multiplication table here: "))

for i in range(1,11):
    print(user * (i))


#Ques_8: Calculate the sum of all numbers from 1 to 100 using a for loop.

sum = 0
for i in range(1,101):
    print(i)
    sum +=i
print(sum)


#Ques_9: Print the following pattern using a for loop:
# *
# **
# ***
# ****

for i in range(1,5):
    print("*"*i)


#Ques_10: Print numbers from 1 to 10 using a while loop.

i = 0
while i<11:
    print(i)
    i = i+1


#Ques_11: Write a program that keeps asking the user to enter a password until they enter the correct one.

password = "Yash"
while True:
    user = input("Enter correct password here: ")
    if user == "Yash":
        print("Correct password, Unlocked!")
        break
    else:
        print("Try again")


#Ques_12: Use a while loop to reverse a given number (e.g., 123 → 321).

num = 123
print(int(str(num)[::-1]))


#Ques_13: Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).

i = 1
for i in range(1,11):
    if i == 7:
        break
    print(i)


#Ques_14: Print numbers from 1 to 10, skipping the number 5 (use continue).
i = 1
for i in range (1,11):
    if i == 5:
        continue
    print(i)


#Ques_15: Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).

i = 1
for i in range(1,6):
    if i == 3:
        pass
    print(i)