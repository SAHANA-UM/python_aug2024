#Program to find biggest (smallest) digit in a number

def find_largest_digit(number):
    largest_digit = 0
    while number > 0:
        digit = number % 10
        if digit > largest_digit:
            largest_digit = digit
            number = number // 10
    return largest_digit

number = int(input("Enter a number: "))

largest_digit = find_largest_digit(number)

print("The largest digit in the number is:", largest_digit)

# Test the function with different inputs

print(find_largest_digit(12345))  # Output: 5
print(find_largest_digit(987654321))  # Output: 9
print(find_largest_digit(0))  # Output: 0
print(find_largest_digit(1111111111))  # Output: 1
print(find_largest_digit(999999999))  # Output: 9

#Note: This program uses a while loop to iterate through each digit of the number, and updates the largest_digit variable if a larger digit is found. It stops iterating once all digits have been checked. This solution has a time complexity of O(n), where n is the number of digits in the input number. The space complexity is O(1), as we are only using a constant amount of additional space to store the largest_digit variable.

