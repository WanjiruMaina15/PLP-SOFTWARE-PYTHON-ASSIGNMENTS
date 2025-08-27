File Operations Script
This Python script demonstrates various file handling operations including reading, writing, and manipulating text files.

📋 Script Overview
The script performs the following operations:

Writes multiple lines to a file called input.txt

Reads and displays the first two characters from the file

Counts characters in the file

Converts content to uppercase

Writes results to an output file

Handles file errors with try-except blocks

🛠️ Functions
1. File Writing
python
with open('input.txt', 'w') as file:
    data = file.writelines([...])
Writes 5 lines of text about programming to input.txt.

2. File Reading
python
with open('input.txt', 'r') as file:
    content = file.readline()[:2]
Reads and prints the first two characters from the first line of the file.

3. Character Counting Function
python
def count_characters(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return len(content)
Returns the total number of characters in the specified file.

4. Uppercase Conversion Function
python
def upper(filename):
    with open('input.txt', 'r') as file:
        data = file.read()
        return data.upper()
Reads a file and returns its content converted to uppercase.

5. Output Writing
python
with open('output.txt', 'w') as file:
    file.write(str(count_characters('input.txt')) + '\n')
    file.write(upper('input.txt'))
Writes the character count and uppercase content to output.txt.

6. Error Handling
python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
Demonstrates proper error handling for missing files.

📁 Files Created
input.txt - Contains the initial text data

output.txt - Contains the processed results (character count and uppercase text)

🚀 Usage
Run the script:

bash
python script_name.py
The script will:

Create input.txt with sample text

Display the first two characters from the file

Print the total character count

Print the uppercase version of the content

Create output.txt with results

Demonstrate error handling for a non-existent file

⚠️ Notes
The script uses proper context managers (with statements) for file handling

Includes error handling for file operations

Converts data types appropriately when writing to files

Closes files properly using context managers

📝 Example Output
After running the script:

Console will show: I (first two characters)

Console will show: 106 (character count)

Console will show uppercase version of the text

output.txt will contain:

text
106
I LOVE PROGRAMMING
PYTHON IS AWESOME
I AM LEARNING JAVASCRIPT
I AM LEARNING HTML
I AM LEARNING CSS
Console will show: The file was not found. (for the missing data.txt)

This script demonstrates fundamental file I/O operations in Python with proper error handling and resource management.

