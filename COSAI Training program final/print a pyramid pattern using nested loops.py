def print_pyramid(height):
    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()


try:
    rows = int(input("Enter the height of the pyramid: "))
    if rows > 0:
        print_pyramid(rows)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
