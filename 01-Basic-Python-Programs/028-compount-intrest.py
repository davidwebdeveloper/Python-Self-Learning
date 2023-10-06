# Compund interest

p = int(input("Enter the principal amount: "))
r = int(input("what is the rate of interest? : ")) / 100
t = int(input("How many times interest calculated?: "))
n = int(input("number of years"))

amount = p*(1 + r/n)**(n*t)
print(amount)
