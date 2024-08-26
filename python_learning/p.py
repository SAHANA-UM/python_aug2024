#count the number of perfect square in N numbers, n is a list

def check_ps(NUMBER):
    root = int(NUMBER ** 0.5)
    if root * root == NUMBER:
        return True
    return False
    

def count_perfect_squares(NUMBERS):
    count = 0
    for NUMBER in NUMBERS :
        if check_ps(NUMBER):
            count = 0
    return count

NUMBER = int(input("Enter the N value:"))

NUMBERS = list()
NUMBERS.append(int(input))

count_perfect_squares = check_ps(NUMBER)

print("Number of perfect squares:", count_perfect_squares)

print("Number of perfect squares:", count_perfect_squares(NUMBERS))


