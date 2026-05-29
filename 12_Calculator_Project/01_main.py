while True: 
    try:
        a = int(input("Enter the first number here: "))
        b = int(input("Enter the second number here: "))

        print("""Types of operations you can done:\n 1. + for addition\n 2. - for substruction\n 3. / for division\n 4. * for multiplication """ )

        o = input("Enter operation: ")
        match o:
            case "+":
                print(f"The result is: {a+b}")
            case "-":
                print(f"The result is: {a-b}")
            case "/":
                print(f"The result is: {a/b}")
            case "*":
                print(f"The result is: {a*b}")
            case default:
                print("Enter the valid operation.")

                


    except Exception as e:


        print("Enter a valid value")