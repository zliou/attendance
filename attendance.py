# attendance.py
# 2016 June 27


from sys import argv


# Functions

def print_usage():
	print "Usage: python attendance.py input_file"


# Check args
if len(argv) != 2:
	print "Incorrect number of arguments."
	print_usage()
	exit();

# Read infile line-by-line, and remove newlines
absent = [line.rstrip('\n') for line in open(argv[1])]

print absent


















