def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            
            print("Invalid input. Please enter a valid integer.")


number = get_integer_input("Enter an integer: ")
print(f"You entered the integer: {number}")
