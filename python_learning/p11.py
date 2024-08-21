#Program to Find Sum of digits of a number

num = int(input('Enter a number to find the sum of digits of:'))
sum = 0

while num > 0:
    sum = sum + num % 10
    num = num // 10
    
print('Sum of digits of the number: ',sum)