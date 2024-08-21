#Program tp print X shape of N lines

def print_x_shape(N):
    # Validate the input
    if not isinstance(N, int) or N <= 0:
        return "Invalid input. Please enter a positive integer."
    
    # Print the X shape
    
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    
    return ""

# Test the function

print(print_x_shape(5))
print(print_x_shape(3))
print(print_x_shape(-2))
print(print_x_shape(0))
print(print_x_shape("abc"))

