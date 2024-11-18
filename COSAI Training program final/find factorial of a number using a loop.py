def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

try:
    num = int(input("Enter a non-negative integer: "))
    result = calculate_factorial(num)
    print(f"The factorial of {num} is {result}.")
except ValueError:
    print("Please enter a valid non-negative integer.")
