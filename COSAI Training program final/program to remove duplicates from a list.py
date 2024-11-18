def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

try:
    elements = input("Enter elements separated by spaces: ").split()
    result = remove_duplicates(elements)
    
    print(f"Original list: {elements}")
    print(f"List after removing duplicates: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
