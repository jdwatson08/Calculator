def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def start():
    print("Welcome to the calculator!")
    print("Please enter two numbers:")
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print("Please choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = int(input("Operation: "))
    if operation == 1:
        print(a, "+", b, "=", add(a, b))
    elif operation == 2:
        print(a, "-", b, "=", subtract(a, b))
    elif operation == 3:
        print(a, "*", b, "=", multiply(a, b))
    elif operation == 4:
        print(a, "/", b, "=", divide(a, b))
    else:
        print("Invalid operation.")
        