import random
import string

def generate_password(length=12):

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    
    password_length = 16  
    password = generate_password(password_length)
    print(f"Generated Password: {password}")
