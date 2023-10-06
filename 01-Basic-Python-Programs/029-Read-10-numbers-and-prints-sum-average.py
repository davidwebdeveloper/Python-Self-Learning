import functools

inputUser = input("Enter the numbers: ")
inputList = inputUser.split()
length = len(inputList)


def convertsNumbers(num):
    return int(num)


finalV = functools.reduce(
    lambda a, b: a+b, list(map(convertsNumbers, inputList)))
print(f"Total = {finalV}")
print(f"Average is = {finalV / length}")
