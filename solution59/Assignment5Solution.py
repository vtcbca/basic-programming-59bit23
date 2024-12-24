# Method 4: Using Recursion
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and make lowercase
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
