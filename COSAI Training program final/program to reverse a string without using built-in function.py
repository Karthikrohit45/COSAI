def reverse_string(s):
    """Reverse the given string without using built-in functions."""
    reversed_str = ""
    # Loop through the string in reverse order and build the reversed string
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage
if __name__ == "__main__":
    input_string = "COSAI"  # Input string
    result = reverse_string(input_string)
    print(f"Reversed string: {result}")
