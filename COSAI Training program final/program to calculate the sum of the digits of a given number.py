def sum_of_digits(number):
    """Calculate the sum of digits of a given number."""
    
    return sum(int(digit) for digit in str(number))

if __name__ == "__main__":
    
    number = 1234 
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is: {result}")
