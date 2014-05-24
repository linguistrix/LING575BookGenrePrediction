__author__ = 'Maria Antoniak'


import sys, os, pickle


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Read in a dictionary of ISBN numbers from the genre file.
isbn_dict = {}
infile_name = 'test_genres.txt'
infile = open(infile_name, 'r')
i = 1
for line in infile:
    if i == 1:
        isbn_dict[line.strip()] = 1
        if len(line.strip().split()) != 1 or not is_number(line.strip()) or len(line.strip()) != 10:
            sys.stderr.write('ERROR: "' + line.strip() + '" is not an ISBN.\n')
    elif i == 3:
        i = 0
    i += 1

# Open the pickled files and filter the reviews by the ISBNs stored in isbn_dict.
pickle_directory_path = 'Books9.pickle'
pickle_file = open(pickle_directory_path, 'r')
object = pickle.load(pickle_file)

# Iterate through all pickled files in directory.
# listing = os.listdir(pickle_directory_path)
# for infile_name in listing:
#     infile = open(pickle_directory_path + infile_name, 'r')



