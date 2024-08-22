#Program to Print X shape inside Hollow Square

number_of_lines=int(input('enter the number of lines to draw the star shaped '))
for i in range(1,number_of_lines+1):
    for j in range(1,number_of_lines+1): 
        if j==1 or j==number_of_lines or i==j or j==number_of_lines-i+1:
            print('*',end=" ") 
        elif i==1 or i==number_of_lines or j==i or i==number_of_lines-j+1: 
            print('*',end=' ') 
        else: 
            print(' ',end=' ')
    print()