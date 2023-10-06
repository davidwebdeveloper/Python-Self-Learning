# Python example to find Student Grade

tamil = float(input("How much marks in Tamil ?"))
english = float(input("How much marks in English ?"))
sub1 = float(input("How much marks in Subject - 1: "))
sub2 = float(input("how much marks in subject - 2 ?: "))
sub3 = float(input("how much marks in subject - 3 ?: "))
sub4 = float(input("How much marks in subject - 4 ?: "))
avg = (tamil+english+sub1+sub2+sub3+sub4)/6
print(f"Average mark is {avg}")
subjects = [tamil, english, sub1, sub2, sub3, sub4]
result = any(subject < 50 for subject in subjects)
print(result)
if result:
    print('U grade')
elif (avg > 90):
    print('A grade')
elif (avg > 80):
    print('B grade')
elif (avg > 70):
    print("C grade")
elif (avg > 60):
    print("D grade")
elif (avg > 50):
    print("E grade")
