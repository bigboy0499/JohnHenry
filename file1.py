# file1.py
def factorial(n):
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        print(f"factorial({n}) = {result}")
        return result

result = factorial(5)
print(f"Factorial of 5 is: {result}")
