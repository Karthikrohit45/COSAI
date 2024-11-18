def read_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read() 
            return contents
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."


file_name = input("Enter the file name to read: ")
result = read_file_contents(file_name)


print(result)
