#Program to find 2nd smallest digit in a number

def find_second_smallest(num):
    # Convert the number into a string to iterate over each digit
    num_str = str(num)
    
    # Initialize the smallest and second smallest variables
    
    smallest = 9
    second_smallest = 9
    
    # Iterate over each digit in the number
    
    for digit in num_str:
        digit = int(digit)
        
        # Update smallest and second smallest if necessary
        
        if digit < smallest:
            second_smallest = smallest
            smallest = digit
        elif digit < second_smallest:
            second_smallest = digit
    
    # Return the second smallest digit
    
    return second_smallest

# Test the function

num = int(input("Enter a number: "))
second_smallest_digit = find_second_smallest(num)
print("The second smallest digit in", num, "is", second_smallest_digit)

# Output: The second smallest digit in 12345 is 2

