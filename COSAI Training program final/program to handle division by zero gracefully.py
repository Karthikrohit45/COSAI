def safe_division(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
    
        return "Error: Division by zero is not allowed."


try:
    num = float(input("Enter the numerator: "))
    den = float(input("Enter the denominator: "))
    
    result = safe_division(num, den)
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid numbers.")
