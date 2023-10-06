# Python example to Calculate Electricity Bill

units = float(input("How much units you used this month? :"))
category = input("Choose any one where you used for: ? \n1. Home\n2. Shop\n")
if category == '1':
    if (units > 100):
        bill = 100 * 2.75    # house below 100 units
        print(f"bill1 = {bill}")
        bill = bill + (units-100) * 3  # above 100 units
    else:
        bill = units * 1.75  # House below 100 units
else:
    bill = units * 3.75  # shop
print(f"Bill = {bill}")
