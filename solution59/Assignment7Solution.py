# Method 4: Using String Multiplication for Formatting
def print_triangle(n):
    for i in range(1, n+1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print numbers
        print(*range(1, 2*i))

input_lines = int(input("Enter the number of rows: "))  # Input number of rows
print_triangle(input_lines)
