import argparse # for user-friendly command line interface. will also automatically generate help and usage messages
import sys # handle exiting script with specific status codes
import os 

def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        print (f"wc-tool: {file_path}: No such file or directory.")
        sys.exit(1)
# Method count_bytes takes a single argument, file_path, which is expected to be the path to the file whose bytes will be counted. Opens the file located at file_path in binary read mode (rb, raw bytes. Good for non text-files) and assigns to variable file. 
# Reads the content of the file and assigns to variable content as a bytes object.
# Returns length of content.
# 'except' statement catches the FileNotFound exception which is raised if file doesn't exist. Exits with status code 1 indicating an error. 

def main():
    parser = argparse.ArgumentParser(description = "wc-tool - word, line, character and byte count")
    parser.add_argument("-c", action = "store_true", help = "print byte count")
    parser.add_argument("file", nargs="?", help = "file to process")

    args = parser.parse_args()

    if not args.c:
        print("Please provide the -c option for byte count.")
        sys.exit(1)
    if not args.file:
        print("Please provide a file to process.")
        sys.exit(1)
    
    byte_count = count_bytes(args.file)
    print (f"{byte_count} {args.file}")

# Initializes a new argument parser object and provides a description of the program when the user invokes the --help option.
# Specifies the -c option to count bytes. If -c is present in the command line, args.c will be set to True. False otherwise.
# Specifies an optional file argument. Will want to support standard input as well.
# Processes an object where each attribute (-c or file) corresponds to a command line argument or option.
# Validates the -c and file options and prints corresponding error messages.
# Calls the count_bytes method passing the filename provided by the user (args.file). Returns the number of bytes, stored in byte_count


if __name__ == "__main__":
    main()
# Checks whether script is being run as the main program, not when imported as a module elsewhere.