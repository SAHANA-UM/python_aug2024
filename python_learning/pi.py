import math

def find_sum_of_odd_elements(NUMBERS):
    sum = 0
    for i in range (0, NUMBERS-1):
        if i % 2 == 0:
            SUM += NUMBERS(i)
    return SUM

NUMBER = int(input("Enter the N value:"))

NUMBERS = []
NUMBERS.append(int(input()))

sum = find_sum_of_odd_elements(NUMBERS)
if sum < 0:
    print('server 1 delocated ',math.abs(SUM) ,'units of memory')
else:
    print('server 1 allocated ',math.abs(SUM),'units of memory')