#Program to check if a number is Perfect Square
import math
num = int(input('Enter a number: '))

#check the input
if num <= 0:
    print("Invalid input!")

root = math.sqrt(num)

if num == root * root:
    print(num,"is a perfect square!")
else:
    print(num ,"is not a perfect square")
