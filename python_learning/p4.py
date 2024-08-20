# Program to accept three distinct numbers and find smallest among them.


num1 = int(input('Enter 1st distinct numbers: '))
num2 = int(input('Enter 2nd distinct numbers: '))
num3 = int(input('Enter 3rddistinct numbers: '))

# check if valid input



if num1 < num2 and num1 < num3:
    print(num1,'is the smallest number')
elif num2 < num3:
    print(num2,'is the smallest number')
else:
    print(num3,'is the smallest number')