def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Contents:\n")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter the file path: ")
read_file(file_path)
