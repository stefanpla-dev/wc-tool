# wc-tool
This is a command line tool designed to mimic the Unix wc-tool in both functionality and user experience, undertaken as a learning exercise. 

The user experience in the command-line is made possible by a command-line arguments object created by argparse. This object stores flags and file path inputs provided by the user either via a file path or standard input (that is, without providing a file path at all and instead inputting directly into the command-line or piping data from another command. Mimicing this functionality required some research as to what standard input even is for the author, yours truly).

Each of the core methods represents a counting algorithm which processes the file in some way. Each implements a linear scan algorithm with O(n) time complexity where the file is read line by line or byte by byte to compute a count of some kind. 

While some work has already gone into optimizing the methods as they were originally written (in the first draft, if you will. See the commit history for more details.), further optimization could be put into the count_bytes(file_path) method to avoid loading the entire file into memory before it is read, perhaps by reading the file in chunks at a time in a similar fashion to how the other methods that count words, lines, and characters read the provided file line by line and keep track of the count in question as it goes. 
