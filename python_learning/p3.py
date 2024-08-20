'''Accept a number as input, say X and define a logic to get the output say Y. 
The input can be only 0 or 1 and the output must be 1 if input is 0 and viceversa'''

X = int(input('Enter the input number(0 and 1 only): '))

# check if the input is valid

# if X == 0 and X == 1
if X >= 0 or X <= 1:
    Y = 1 - X
    print('the inverse of X is ',Y)    
