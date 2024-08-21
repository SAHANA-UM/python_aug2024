#Program to check if a number is Perfect Square
import math
input_num = int(input('Enter a number to check if it is a perfect square: '))

#check the input
if input_num <= 0:
    print("Invalid input!")

root_num = math.sqrt(input_num)

root_num = math.floor(root_num)

product = root_num * root_num

if product == input_num :
    print(input_num,"is a perfect square!")
else:
    print(input_num ,"is not a perfect square")
