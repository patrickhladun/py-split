import sys
import pyperclip

def get_first_line(input_string, max_length, first_line_adjustment=4):
    words = input_string.split()

    first_piece = ''
    second_piece = ''
    current_length = 0
    total = max_length - first_line_adjustment

    for word in words:
        word_length = len(word) + 1
        if current_length + word_length <= total:
            if first_piece:
                first_piece += ' ' + word
            else:
                first_piece = word
            current_length += word_length
        else:
            if second_piece:
                second_piece += ' ' + word
            else:
                second_piece = word

    return first_piece, second_piece

def get_lines_from_string(input_string, max_length):
    words = input_string.split()
    lines = []
    current_line = ''
    current_length = 0

    for word in words:
        word_length = len(word) + 1
        if current_length + word_length <= max_length:
            if current_line:
                current_line += ' ' + word
            else:
                current_line = word
            current_length += word_length
        else:
            lines.append(current_line)
            current_line = word
            current_length = word_length

    if current_line:
        lines.append(current_line)
    return lines

def format_text(input_string, max_length):
    first_piece, second_piece = get_first_line(input_string, max_length)
    lines = get_lines_from_string(second_piece, max_length)

    formatted_text = '"' + first_piece + ' "\n'
    for line in lines:
        formatted_text += '"' + line + ' "\n'

    print(formatted_text)
    pyperclip.copy(formatted_text.strip())  # Copy to clipboard without the last newline

if len(sys.argv) != 3:
    print("Usage: python split_string.py <input_string> <max_length>")
    sys.exit(1)

input_string = sys.argv[1]
max_length = int(sys.argv[2])

format_text(input_string, max_length)
