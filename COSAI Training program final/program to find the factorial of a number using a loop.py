def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"The factorial of {number} is: {factorial(number)}")
