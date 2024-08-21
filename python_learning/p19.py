'''
Program to print the Right angled Triangle of N lines
*
**
***
****
*****
'''

height = int(input('Enter the number of rows of right angled triangle: '))
for i in range(0,height):
    for j in range(0,i+1):
        print('*', end=' ')
    print()