# attendance.py
# 2016 June 27


from sys import argv


# Functions ##########


# Prints usage
def print_usage():
	print "Usage: python attendance.py input_file"


# Prints help
def print_help():
	print "Manual coming soon."


# Prints values in organized rows, separated by spaces
# @param values		A list of values to print
def show(values):
	
	# Constants
	NAMES_PER_LINE = 3
	SPACING = 24

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
			row += " "
		for i in range (0, num_spaces):
			row += " "
		if (num_printed % NAMES_PER_LINE) == 0:
			print row
			row = ""


# Check args ##########
if len(argv) != 2:
	print "\nIncorrect number of arguments."
	print_usage()
	print ""
	exit();

# TODO: v2 - takes a second file of people present

# Read infile line-by-line, and remove newlines
raw = [line.rstrip('\n') for line in open(argv[1])]
roster = [name.replace('\t', ' ') for name in raw]

# Init rosters and other attendance vars
absent = roster
present = [];
prompt = "> "
done = False

# Prompt input for member names
print ("\nEnter names of members to mark PRESENT."
	"\n\tKeywords: (sans-quotes)"
	"\n\t\t'help' for this program's manual."
	"\n\t\t'undo' to undo the last action."
	"\n\t\t'done' to finish inputting names.")

while not done:
	member = raw_input(prompt)
	if member == "done":
		break
	elif member == "undo":
		print "Undo function is not yet implemented"
	elif member == "help":
		print_help()

# Print names of members present and absent
print("\n##################################"
	"\nThe following members are PRESENT:\n")
if (len(present) == 0):
	print "No members are present."
else:
	show(present)

print("\n##################################"
	"\nThe following members are ABSENT:\n")
if (len(absent) == 0):
	print "No members are absent. Hooray!"
else:
	show(absent)

print "##################################\n"
















