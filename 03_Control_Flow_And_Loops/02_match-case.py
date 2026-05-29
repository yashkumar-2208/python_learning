#Match-Case 

a = int(input("Enter a number between 1 and 30: "))

match a:
    case 12:
        print("You won a laptop!")
    case 29:
        print("You won a tablet!")
    case 20:
        print("You won a smartphone!")
    case _:
        print("Bad luck!")

