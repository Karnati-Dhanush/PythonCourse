def calculator(x, y, operation):
    if operation == "ADD":
        print("Sum of {0} and {1} is {2}".format(x, y, x + y))
    elif operation == "SUBTRACT":
        print("Subtraction of {0} and {1} is {2}".format(x, y, x - y))
    elif operation == "MULTIPLY":
        print("multiplication of {0} and {1} is {2}".format(x, y, x * y))
    elif operation == "DIVIDE":
        print("division of {0} and {1} is {2}".format(x, y, x / y))
    else:
        print("the operation is INVALID")


calculator(2, 5, "MULTIPLY")

