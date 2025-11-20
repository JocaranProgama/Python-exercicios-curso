def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

def exponent(a, b):
    return a ** b


operations = {
    '+': sum,
    '*': multiply,
    '/': divide,
    '-': subtract,
    '': exponent
}

while True:
    chosen_operator = input("Choose an operation (+, -, *, /, **) or 'q' to quit: ")

    if chosen_operator == 'q':
        print("Exiting calculator.")
        break

    if chosen_operator not in operations:
        print("Invalid operation. Please try again.\n")
        continue

    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    result = operations[chosen_operator](n1, n2)
    print(f"Result: {n1} {chosen_operator} {n2} = {result}\n")
    