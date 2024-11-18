def sum_of_numbers(numbers):
    return sum(numbers)

try:
    user_input = input("Enter numbers separated by spaces: ")
    number_list = list(map(float, user_input.split()))
    
    total = sum_of_numbers(number_list)
    print(f"The sum of the numbers {number_list} is {total}.")
except ValueError:
    print("Please enter valid numbers separated by spaces.")
