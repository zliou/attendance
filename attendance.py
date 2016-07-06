# attendance.py
# 2016 June 27


from sys import argv


# Constants ##########

NAMES_PER_LINE = 3
SPACING = 24


# Functions ##########


# Prints usage
def print_usage():
	print "Usage: python attendance.py input_file"


# Prints help
def print_help():
	print "Manual coming soon."


def config():
	print ("SETTINGS ----------"
		"\n\tKeywords:"
		"\n\t\t'line' to change the number of names per line"
		"\n\t\t'space' to change the space allocated to each name"
		"\n\t\t'finish' to return to name input mode.")

	prompt = "(SETTINGS)>"
	done = False
	while not done:
		# TODO: catch non-integer cases
		option = raw_input(prompt)
		if option == "line":
			line = raw_input("Enter number of names per line:")
			NAMES_PER_LINE = int(line)
		elif option == "space":
			space = raw_input("Enter spacing:")
			SPACING = int(space)
		elif option == "finish":
			done = True
		else:
			print "Invalid option."
	


# Prints values in organized rows, separated by spaces
# @param values		A list of values to print
def show(values):
	
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
		if ((num_printed % NAMES_PER_LINE) == 0) or (value == values[-1]):
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
present = list()
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
	elif member == "config":
		config()
	elif member in absent:
		present.append(member)
		present.sort()
		absent.remove(member)
	else:
		print member, " not found."
		
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
















