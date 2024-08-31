import pdb
pdb.set_trace()

def find_sum_of_digits(num):
    sum = 0
    while num != 0:
        reminder = num % 10
        num = num // 10
        sum += reminder
    return sum
input_number = int(input('Enter a number to find the sum of digits: '))
sum_of_digits = find_sum_of_digits(input_number)
print('Sum of digits of',input_number,'is',sum_of_digits)