def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  
    return True  


if __name__ == "__main__":
    number = 13  
    result = is_prime(number)
    print(f"Is {number} a prime number? {result}")
