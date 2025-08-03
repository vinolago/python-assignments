while True:

    a =float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c= input("Now type any mathematical operation (+, -, *, or /) ")

    if c == "+":
        result = a+b
    elif c == "-":
        result = a-b
    elif c == "*":
        result= a*b
    elif c == "/":
        if b!=0:
            result=a/b
        else:
            result = "Error. Division by 0 not possible."
    else:
        result="Unknown operation."

    print(f"This is your result: {result}")

    again=input("Would you like to go again?(yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break