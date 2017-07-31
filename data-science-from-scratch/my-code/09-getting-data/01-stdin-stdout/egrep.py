# * stdin and stdout
#   - Running script from the command line, you can pipe data via these
#   sys methods

# egrep.py
import sys
import re

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]

# for every line passed into the script
for line in sys.stdin:
    # if it matched the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)
