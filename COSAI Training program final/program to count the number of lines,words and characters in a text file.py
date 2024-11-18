def count_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines() 
            num_lines = len(lines)  
            num_words = 0
            num_chars = 0
            
            for line in lines:
                num_words += len(line.split())  
                num_chars += len(line)  
            
            return num_lines, num_words, num_chars
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None, None, None
    except IOError:
        print(f"An error occurred while reading the file {filename}.")
        return None, None, None

file_name = input("Enter the filename to analyze: ")

lines, words, chars = count_file_contents(file_name)

if lines is not None:
    print(f"The file {file_name} contains:")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")
