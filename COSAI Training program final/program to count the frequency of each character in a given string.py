from collections import Counter

def count_characters(s):
    """Count the frequency of each character in the string."""
    return dict(Counter(s))


if __name__ == "__main__":
    input_string = "success"  
    result = count_characters(input_string)
    print(result)
