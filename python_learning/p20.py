'''
Program to print the Equi Lateral Triangle of N lines
    *
   ***
  *****
 *******
*********
'''

num_rows = int(input('Enter the number of rows of right angled triangle: '))
k = 2 * num_rows + 2
for i in range(1,num_rows+1):
    for j in range(0,k):
        print(end=' ')
    k = k - 1
    for j in range(0, i ):
        print('*',end=' ')
    print()