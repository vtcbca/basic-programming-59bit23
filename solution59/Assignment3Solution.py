def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Test the function
terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence (first {terms} terms): {list(fibonacci_generator(terms))}")