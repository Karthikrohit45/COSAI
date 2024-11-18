def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    
 
    a = a + b
    b = a - b
    a = a - b
    
    print(f"After swapping: a = {a}, b = {b}")
    return a, b


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
swap_numbers(x, y)
