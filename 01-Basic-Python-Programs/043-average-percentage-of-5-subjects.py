# Python program to find Total Average & Percentage of 5 Subjects
import functools

subjects = input("Enter the Five subject marks in sequence with space:  ")
subjectsList = subjects.split()
total = functools.reduce(
    lambda a, b: a+b, list(map(lambda a: int(a), subjectsList)))
print(f'Total = {total}')
print(f'Avg = {total / len(subjectsList)}')
