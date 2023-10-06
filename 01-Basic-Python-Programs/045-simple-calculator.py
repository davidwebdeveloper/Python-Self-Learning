# Python Program to Make a Simple Calculator

def addition(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


operation = input(
    "Enter your choice ? \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n:")

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
if (operation == '1'):
    result = addition(a, b)
elif (operation == '2'):
    result = sub(a, b)
elif (operation == '3'):
    result = mul(a, b)
elif (operation == '4'):
    result = div(a, b)
else:
    print("You choose wrong operation")

print(f"Result is = {result}")
