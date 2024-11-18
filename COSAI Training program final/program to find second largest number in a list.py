def second_largest(numbers):
    unique_numbers = set(numbers)

        if len(unique_numbers) < 2:
        return None
    
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]

try:
    numbers_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    
    result = second_largest(numbers_list)
    if result is not None:
        print(f"The second largest number is {result}.")
    else:
        print("There are fewer than 2 unique numbers in the list.")
except ValueError:
    print("Please enter valid integers.")
