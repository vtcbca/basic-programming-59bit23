# Method 4: Using String Multiplication and Concatenation
def print_pattern(n):
    for i in range(1, n+1):
        # Print leading spaces
        line = ' ' * (n - i)
        
        # Add increasing characters
        for j in range(1, i+1):
            line += chr(64 + j) + " "
        
        # Add decreasing characters
        for j in range(i-1, 0, -1):
            line += chr(64 + j) + " "
        
        # Print the formed line
        print(line.strip())

input_lines = int(input("Enter the number of lines: "))  # Input number of rows
print_pattern(input_lines)
