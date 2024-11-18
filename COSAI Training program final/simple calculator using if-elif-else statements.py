def calculator():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
   
    choice = input("Enter your choice (1/2/3/4): ")

 
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            print(f"The result of {num1} + {num2} is {num1 + num2}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} is {num1 - num2}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} is {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result of {num1} / {num2} is {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select a valid operation.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


calculator()
