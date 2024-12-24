def factorial_while_loop(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Test the function
number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial_while_loop(number)}")