def count_word_frequency(input_string):
    words = input_string.lower().split()
    
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    
    return frequency_dict

input_text = input("Enter a string: ")

word_frequencies = count_word_frequency(input_text)


print("Word Frequencies:")
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
