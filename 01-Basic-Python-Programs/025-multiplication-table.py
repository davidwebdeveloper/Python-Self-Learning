# Python program for Multiplication Table

number = int(input("Enter your multiplication table no: "))
limit = int(input("Enter the limit: "))
for i in range(1, limit+1):
    print(f"{i} * {number} = {i*number}")
