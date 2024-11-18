def determine_data_type(data):
    """Function to identify the data type of the given input."""
    if isinstance(data, int):
        return "Integer"
    elif isinstance(data, float):
        return "Float"
    elif isinstance(data, str):
        return "String"
    elif isinstance(data, list):
        return "List"
    elif isinstance(data, tuple):
        return "Tuple"
    elif isinstance(data, dict):
        return "Dictionary"
    else:
        return "Unknown type"

while True:
    user_input = input("Enter a value (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting the program.")
        break

    try:
        evaluated_input = eval(user_input)
    except:
        evaluated_input = user_input
    data_type = determine_data_type(evaluated_input)
    print(f"The data type of the input is: {data_type}")
