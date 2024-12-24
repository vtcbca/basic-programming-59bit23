def is_prime_while_loop(n):
    if n <= 1:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

# Test the function
number = int(input("Enter a number: "))
if is_prime_while_loop(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")