import os

def extract_level(entry):
    level_index = entry.find("Level ")
    if level_index != -1:
        level = entry[level_index + 6:]
        return int(level) if level.isdigit() else -1
    return -1

# Get the script's current directory
script_dir = os.path.dirname(__file__)

# Define the relative paths to input and output files
input_file_path = os.path.join(script_dir, "inputList.txt")
output_file_path = os.path.join(script_dir, "outputList.txt")

# Read the unsorted data from the input file
with open(input_file_path, "r") as file:
    data = file.read().splitlines()

# Sort the data by levels in descending order
sorted_data = sorted(data, key=extract_level, reverse=True)

# Write the sorted data to the output file
with open(output_file_path, "w") as file:
    for entry in sorted_data:
        file.write(entry + "\n")
