import random
import string

def generate_password(length=8):
    if length < 8:
        raise ValueError("Password must be at least 8 characters long.")
    
    # Character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all categories
    all_characters = uppercase + lowercase + digits + special
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to randomize character positions
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length (minimum 8): "))
        password = generate_password(password_length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
