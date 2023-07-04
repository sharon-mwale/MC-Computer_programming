def factorial(n):
    # factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        #  factorial of n is n times factorial of (n-1)
        return n * factorial(n - 1)
result = factorial(5)
print(result)  # Output: 120
