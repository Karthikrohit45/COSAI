import os

input_file = '/Users/karthik/Desktop/untitled folder 5/input.txt'

if os.path.exists(input_file):
    print(f"File '{input_file}' exists and is accessible.")
else:
    print(f"File '{input_file}' does NOT exist.")
def filter_adults(input_file, output_file):
    
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        # Filter names of people over 18
        adults = []
        for line in lines:
            name, age = line.strip().split(', ')
            if int(age) > 18:
                adults.append(name)
        
        # Write the names of adults to the output file
        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(adults))
        
        print(f"Filtered names written to {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_file = '/Users/karthik/Desktop/untitled folder 5/input.txt'
output_file = '/Users/karthik/Desktop/untitled folder 5/output.txt'

filter_adults(input_file, output_file)
