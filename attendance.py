# attendance.py
# 2016 June 27


from sys import argv


# Functions ##########


# Prints usage
def print_usage():
	print "Usage: python attendance.py input_file"


# Prints values in organized rows, separated by spaces
# @param values		A list of values to print
def show(values):
	
	# Constants
	NAMES_PER_LINE = 3;
	TAB_WIDTH = 8
	SPACING = NAMES_PER_LINE * TAB_WIDTH

	# Init vars
	row = ""
	num_printed = 0;

	# Loop through each value
	for value in values:

		# Add value to row and increment counter
		row += value 
		num_printed += 1

		# Print spaces for spacing
		num_spaces = SPACING - len(value)
		if num_spaces < 1:
			print " "
		for i in range (0, num_spaces):
			row += ' '
		if (num_printed % NAMES_PER_LINE) == 0:
			print row
			row = ""


# Check args ##########
if len(argv) != 2:
	print "\nIncorrect number of arguments."
	print_usage()
	print ""
	exit();

# Read infile line-by-line, and remove newlines
raw = [line.rstrip('\n') for line in open(argv[1])]
roster = [name.replace('\t', ' ') for name in raw]


show(roster);

















