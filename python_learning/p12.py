#Program to Find count of digits of a number

input_num = int(input('Enter a number to find the count of digits: '))
count = 0
num = input_num
while num > 0:
    num = num // 10
    count = count + 1
    
print('The count of digits in the',num,'is:', count)