def read_file(file_name):
    try:
        # Try to open and read the file
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{file_name}' was not found.")

# Example usage
if __name__ == "__main__":
    # Replace 'example.txt' with the file you want to test
    file_name = input("Enter the file name: ")
    read_file(file_name)
