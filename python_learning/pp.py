import pdb
pdb.set_trace()


def find_factorial_iteratively(num):
    factorial_number = 1
    if num == 0 or num == 1:
        return factorial_number
    for i in range(2, num+1):
        factorial_number = factorial_number * i
    return factorial_number
        
def find_factorial_recursively(num):
    if num == 0 or num == 1:
        return 1
    return num * find_factorial_iteratively(num-1)

input_number = int(input("Enter a number to find its factorial: "))

choice = int(input('1.Iterative 2.Recursive . Your choice please: '))

factorial_number = 0
if choice == 1:
    factorial_number = find_factorial_iteratively(input_number)
else:
    factorial_number = find_factorial_recursively(input_number)
    
print("Factorial of", input_number, "is", factorial_number)