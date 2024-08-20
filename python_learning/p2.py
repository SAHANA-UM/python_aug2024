#To read data from the console, we can use input (). However the input() always reads only a string as usual with all other languages

#We must 1st cast(covert) the string into a number(specifically an int)

# The 


my_number = int(input('Enter a number to check if it is Even or not: '))

print(type(my_number))

if my_number % 2 == 0:
    print(my_number,'is an Even number')
else:
    print(my_number,'is not an Even number')