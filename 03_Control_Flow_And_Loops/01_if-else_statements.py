#Driving age testing program.
while True:
    age = int(input("Enter your age here: "))

    if (age>18):
        print("You can drive.")
    elif (age<18):
        print("You can not drive.")
    elif (age==18):
        print("Let's make your license.")
    elif (age==0):
        print("You're not born yet.")
    elif (age>=0):
        print("Are you serious?")

    else:
        print("Invalid input!")