# py-split

# Split String Script

This script is designed to split a long string into multiple lines of a specified maximum length, maintaining word integrity. It's useful for formatting text in environments where long lines need to be broken up, such as in code or when generating formatted output.

## How to Use

1. **Installation:**
   - Ensure you have Python installed on your system.
   - Download the script to your desired location.

2. **Usage:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python with the following command:
     ```
     python split_string.py <input_string> <max_length>
     ```
     Replace `<input_string>` with the text you want to split and `<max_length>` with the maximum length of each line.

3. **Example:**
   - Suppose you want to split the string "This is a long sentence that needs to be split into multiple lines." into lines with a maximum length of 20 characters. You would run:
     ```
     python split.py "This is a long sentence that needs to be split into multiple lines." 20
     ```

4. **Output:**
   - The script will print the split text to the console.

## Notes
- Ensure that the input string and maximum length are provided as command-line arguments.
- The script splits the string by words, ensuring that no word is split across lines.