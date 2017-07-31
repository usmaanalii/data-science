# * The Basics of Text Files
import Counter
#   - Obtain a file object using -> open

# 'r' means read-only
file_for_reading = open('reading_file.txt', 'r')

# 'w' is write -- will destroy the file if already exists!
file_for_writing = open('writing_file.txt', 'w')

# 'a' is append -- for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')

# don't forget to close your files when you're done
file_for_writing.close()

# It's easy to forget to close your files, so use them in a with block
with open(filename, 'r') as f:
    data = function_that_gets_data_from(f)

# at this point f has already been closed, so don't try to use it
process(data)

# reading a whole text file by iterating with a for loop
starts_with_hash = 0

with open('input.txt', 'r') as f:
    for line in file:
        if re.match('^#', line):
            starts_with_hash += 1

# you may need to split newline (\n) characters


# Example: email file to create a histogram of domains
def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]


with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if '@' in line)
