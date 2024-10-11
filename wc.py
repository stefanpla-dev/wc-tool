import argparse # for user-friendly command line interface. will also automatically generate help and usage messages
import sys # handle exiting script with specific status codes
import os 

def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            byte_content = file.read()
            return len(byte_content)
    except FileNotFoundError:
        print (f"wc-tool: {file_path}: No such file or directory.")
        sys.exit(1)
# Method count_bytes takes a single argument, file_path, which is expected to be the path to the file whose bytes will be counted. Opens the file located at file_path in binary read mode (rb, raw bytes. Good for non text-files) and assigns to variable file. 
# Reads the content of the file and assigns to variable content as a bytes object.
# Returns length of content.
# 'except' statement catches the FileNotFound exception which is raised if file doesn't exist. Exits with status code 1 indicating an error. 

def count_lines(file_path):
    try:
        with open (file_path, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"wc-tool: {file_path}: No such file or directory.")
        sys.exit(1)
# Very similar to count_bytes method. Differences here are opening the file in text mode ('r') so line breaks can be counted like characters.
# At first was counting the number of \n characters, but this could count empty lines as a line (which I, the author, personally do not want). This also requires the entire file be loaded before counting instead of summing the lines as you go - more memory efficient. 

def count_words(file_path):
    word_count = 0
    try:
        with open (file_path, 'r', encoding = 'utf-8') as file:
            for line in file:
                words = line.split()
                word_count += len(words)
        return word_count
    except FileNotFoundError:
        print(f"wc-tool: {file_path}: No such file or directory.")
        sys.exit(1)
# Each new method is easier to write than the last seeing as they all riff on each other a bit. 
# Was originally reading the entire file into memeory, and using a .split() method to count the length of the file, but this could be space and time inefficient if the file were enormous (the test file in this directory is very small). Optimized above.

def main():
    parser = argparse.ArgumentParser(description = "wc-tool - word, line, character and byte count")
    parser.add_argument("-c", action = "store_true", help = "Count and print the number of bytes in a file.")
    parser.add_argument("-l", action = "store_true", help = "Count and print the number of lines in a file.")
    parser.add_argument("-w", action = "store_true", help = "Count and print the number of words in a file.")
    parser.add_argument("file", nargs="?", help = "Path to the file to process.")

    args = parser.parse_args()

    if not (args.c or args.l or args.w):
        print("Please provide at least one option (-c or -l).")
        sys.exit(1)

    if not args.file:
        print("Please provide a file to process.")
        sys.exit(1)
    
    output = []

    if args.l:
        line_count = count_lines(args.file)
        output.append(f"{line_count}")
    if args.c:
        byte_count = count_bytes(args.file)
        output.append(f"{byte_count}")
    if args.w:
        word_count = count_words(args.file)
        output.append(f"{word_count}")

    output.append(args.file)
    print(" ".join(output))

# Initializes a new argument parser object and provides a description of the program when the user invokes the --help option.
# Specifies the -c option to count bytes. If -c is present in the command line, args.c will be set to True. False otherwise. This is true for other functionality as well (line counts, word counts, character counts).
# Specifies an optional file argument. Will want to support standard input as well.
# Processes an object where each attribute (-c, -l or file) corresponds to a command line argument or option.
# Output to the command line depends on the action performed and will only print what is specifically requested by the user.


if __name__ == "__main__":
    main()
# Checks whether script is being run as the main program, not when imported as a module elsewhere.